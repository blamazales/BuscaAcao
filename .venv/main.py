from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import pandas as pd

# Entrada do usuário para o código da ação
#codigo_acao = input("Digite o código da ação (ex: PETR3.SA): ")

# Inicializar o WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Acessar o site de cotações
driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

data_hora = list()
codigo_acao = ['PETR3.SA','MGLU3.SA','VIVT3.SA']
valores = list()

for empresa in codigo_acao:
    # Encontrar o campo de busca e inserir o valor digitado pelo usuário
    input_busca = driver.find_element(By.ID, 'filled-normal')
    input_busca.send_keys(codigo_acao)
    sleep(10)

    # Pressionar Enter após inserir o código da ação
    input_busca.send_keys(Keys.ENTER)
    sleep(10)

    # Capturar o valor da cotação da ação
    span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
    cotacao_valor = span_val.text
    data_hora.append(datetime.now().strftime('%d%m%Y %H:%M:%S'))

    # Exibir o valor da cotação
    #print(f'Valor da cotação da {codigo_acao}: {cotacao_valor}')
    print(codigo_acao)
    print(valores)
    print(data_hora)

dados = {
    'empresa':codigo_acao,
    'valor': valores,
    'data_hora': data_hora,
}

print(dados)

df_empresas = pd.DataFrame(dados)
df_empresas.to_excel('./empresas.xlsx')
    #input('')
    # Encerrar o navegador
    #driver.quit()
