# funcoes_analise.py

import pandas as pd
import numpy as np

def rmse(y_true, y_pred):
    """
    Calcula a Raiz do Erro Quadrático Médio (Root Mean Square Error - RMSE).

    Args:
        y_true (pd.Series or np.array): Valores verdadeiros (medidos).
        y_pred (pd.Series or np.array): Valores previstos pelo modelo.

    Returns:
        float: O valor do RMSE.
    """
    return np.sqrt(np.mean((y_true - y_pred) ** 2))

def calcdist(dist_horizontal):
    """
    Calcula a distância euclidiana a partir de uma distância horizontal,
    considerando uma altura vertical fixa de 2.87 metros.

    Esta função é específica para cenários onde há uma elevação vertical
    constante entre o transmissor e o receptor.

    Args:
        dist_horizontal (float or pd.Series): A distância no plano horizontal.

    Returns:
        float or pd.Series: A distância euclidiana total.
    """
    altura_fixa = 2.87
    distancia_total = np.sqrt(altura_fixa**2 + dist_horizontal**2)
    return distancia_total

def txt_to_csv(input_file, output_file, is_full3d=False):
    """
    Converte um arquivo de dados de simulação (TXT) para o formato CSV.

    A função lê um arquivo de texto com colunas separadas por espaços e o salva
    como um arquivo CSV com cabeçalhos apropriados, facilitando a manipulação
    com o pandas.

    Args:
        input_file (str): O caminho para o arquivo TXT de entrada.
        output_file (str): O caminho onde o arquivo CSV será salvo.
        is_full3d (bool): Se True, usa os cabeçalhos para o modelo Full3D.
                          Se False, usa cabeçalhos para outros modelos simulados.
    """
    data = pd.read_csv(input_file, delim_whitespace=True, header=None)

    if is_full3d:
        data.columns = ['ID', 'X', 'Y', 'Z', 'Distance (m)', 'Power (dBm)', 'Phase']
        data = data.astype({
            'Distance (m)': int,
            'Power (dBm)': float,
            'Phase': float
        })
    else:
        # Ajuste as colunas conforme o formato do seu outro arquivo simulado
        data.columns = ['ID', 'X', 'Y', 'Z', 'Distance (m)', 'Pl']
        data = data.astype({
            'Distance (m)': int,
            'Power (dBm)': float,
            'Phase': float
        })

    data.to_csv(output_file, index=False)
    print(f"Arquivo '{output_file}' foi salvo com sucesso!")


def float_intercept(dados):
    """
    Implementa o modelo de perda de percurso "Floating Intercept" (FI) ou Alpha-Beta.

    Este modelo é uma generalização do modelo de log-distância e não fixa o
    intercepto. Ele determina os coeficientes alpha e beta através de regressão linear.

    Args:
        dados (pd.DataFrame): DataFrame contendo os dados de medição.
                              A primeira coluna deve ser a distância (d).
                              A terceira coluna deve ser a perda de percurso (pl).

    Returns:
        tuple: Uma tupla contendo:
            - fi (np.array): Perda de percurso calculada pelo modelo FI.
            - alfa (float): O intercepto do modelo (parâmetro alpha).
            - beta (float): O coeficiente de inclinação do modelo (parâmetro beta).
    """
    d = dados.iloc[:, 0]
    pl = dados.iloc[:, 2]

    # Cálculo de beta (inclinação)
    logd = 10 * np.log10(d)
    b = (np.sum(logd)) ** 2
    a = np.sum(logd ** 2)
    den_beta = a - (b / len(logd))
    num_beta = np.sum((logd * pl)) - ((np.sum(logd) * np.sum(pl)) / len(logd))
    beta = num_beta / den_beta

    # Cálculo de alfa (intercepto)
    y_mean = np.mean(pl)
    x_mean = np.mean(logd)
    alfa = y_mean - beta * x_mean

    # Cálculo da perda de percurso modelada (FI)
    fi = alfa + beta * logd

    # Cálculo do Erro Quadrático Médio (RMSE) e shadowing
    mse = np.sqrt(np.mean((pl - fi) ** 2))
    shadowing_std = np.std(pl - fi)

    print(f"--- Modelo Floating Intercept (FI) ---")
    print(f"RMSE: {mse:.4f}")
    print(f"Alpha: {alfa:.4f}")
    print(f"Beta: {beta:.4f}")
    print(f"Shadowing (Std Dev): {shadowing_std:.4f}")

    return fi, alfa, beta

def close_in(dados, freq_ghz=3.5, dist_ref=1.0):
    """
    Implementa o modelo de perda de percurso "Close-In" (CI) com distância de referência.

    Este modelo utiliza uma medição de referência a uma curta distância (d0)
    para prever a perda em distâncias maiores. Ele é útil para calcular o
    expoente de perda de percurso (Path Loss Exponent - PLE).

    Args:
        dados (pd.DataFrame): DataFrame contendo os dados de medição.
                              A primeira coluna deve ser a distância (d).
                              A terceira coluna deve ser a perda de percurso (L).
        freq_ghz (float): Frequência do sinal em GHz.
        dist_ref (float): Distância de referência (d0) em metros.

    Returns:
        tuple: Uma tupla contendo:
            - ci (np.array): Perda de percurso calculada pelo modelo CI.
            - ple (float): O expoente de perda de percurso (n).
    """
    c = 3e8  # Velocidade da luz em m/s
    freq_hz = freq_ghz * 1e9
    wavelength = c / freq_hz

    d = dados.iloc[:, 0]
    L = dados.iloc[:, 2]

    # Perda de percurso no espaço livre na distância de referência d0
    L0 = 20 * np.log10((4 * np.pi * dist_ref) / wavelength)

    # Regressão linear para encontrar o PLE (n)
    D = 10 * np.log10(d / dist_ref)
    D_reshaped = np.array(D).reshape(-1, 1)
    
    # Usando np.linalg.lstsq para resolver a regressão para 'n'
    ple, _, _, _ = np.linalg.lstsq(D_reshaped, (L - L0), rcond=None)
    ple = ple[0]

    # Cálculo da perda de percurso modelada (CI)
    ci = L0 + 10 * ple * np.log10(d / dist_ref)

    # Cálculo do Erro Quadrático Médio (RMSE) e shadowing
    mse = np.sqrt(np.mean((L - ci) ** 2))
    shadowing_std = np.std(L - ci)

    print(f"\n--- Modelo Close-In (CI) ---")
    print(f"RMSE: {mse:.4f}")
    print(f"Path Loss Exponent (PLE): {ple:.4f}")
    print(f"Shadowing (Std Dev): {shadowing_std:.4f}")

    return ci, ple