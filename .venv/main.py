from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import pandas as pd

options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

empresas = ['PETR3.SA', 'MGLU3.SA', 'VIVT3.SA']
valores = list()
data_hora = list()

for empresa in empresas:
    input_busca = driver.find_element(By.ID, 'filled-normal')
    input_busca.send_keys(empresa)
    sleep(2)

    input_busca.send_keys(Keys.ENTER)

    span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
    cotacao_valor = span_val.text
    
    valores.append(cotacao_valor)
    data_hora.append(datetime.now().strftime('%d%m%Y %H:%M:%S'))
    print(f'Empresa: {empresa}')

dados = {
    'empresa': empresas,
    'valor': valores,
    'data_hora': data_hora,
}    

print(dados)

df_empresas = pd.DataFrame(dados)
df_empresas.to_excel('./empresas.xlsx', index=False)
#df_empresas.to_excel('./empresas-acoes.xls', index=False)
    #print(f'Valor da cotação: {cotacao_valor}')

#print(empresas)
#print(valores)
#print(data_hora)

#input('')