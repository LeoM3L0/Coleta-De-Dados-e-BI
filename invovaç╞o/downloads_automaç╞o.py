from login import *
from Funções_em_diretórios import *
import time

#Verificando se existe a pasta que o programa vai utilizar
with alive_bar(1) as bar:
    for i in range(1):
        time.sleep(0.1)
        bar()
        if i == 0:
            if 'guiaOrto' in os.listdir('C:\\'):
                print('Diretorio já criado')
            else:
                #Criando o diretório que nosso programa irá utilizar
                print("Criando diretorio")
                Criacao_de_diretorio_e_pastas_do_Programa()

#Chamando função que tira todos as planilhas que nossa automação gerou do diretório de DOWNLOADS
Limpeza_de_downloads_antigos() 

#Chamando função que tira todos as planilhas que nossa automação gerou na ultima vez que rodou!
Limpeza_da_pasta_do_programa()

driver.switch_to.new_window('tab')
driver.get("https://guiaodonto.com/home/dash")


driver.find_element(by=By.CLASS_NAME, value='pe-7s-users').click()
time.sleep(3)

print("\n--BAIXANDO PLANILHA 1--")
with alive_bar(1) as bar:
    for i in range(1):
        time.sleep(3)
        bar()
        if i == 0:
            driver.find_element(by=By.XPATH, value='//*[@id="excel"]/span').click()

time.sleep(3)

driver.close()

driver.switch_to.window(original_window)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/button').click()

lista_filtro = driver.find_element(By.ID, 'lista-consulta')
lista_filtro.click()

# data_inicial = driver.find_element(By.XPATH, '//*[@id="data_inicial"]')
# data_inicial.click()
# data_inicial.send_keys(inicio)

# data_final = driver.find_element(By.XPATH, '//*[@id="data_final"]')
# data_final.click()
# data_final.send_keys(fim)

driver.find_element(By.XPATH, '//*[@id="filtro"]/form/div[4]/div/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="filtro"]/form/div[4]/div/div[2]/div/div[4]').click() # Selecionar Dentista
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[4]/form/div[14]/button').click() # Selecionar Filtrar

driver.find_element(By.CLASS_NAME, 'btn.btn-danger.btn-block.btn-block.btn-fill.dropdown-toggle').click() #Clicar para achar Planilha
print("\n--BAIXANDO PLANILHA 2--")
with alive_bar(1) as bar:
    for i in range(1):
        time.sleep(3)
        bar()
        if i == 0:
            driver.find_element(By.PARTIAL_LINK_TEXT, 'Exportar em Excel').click() #Baixar Planilha
time.sleep(3)

#Chamando função que move todas as planilhas baixadas para pasta do programa
Mover_arquivos_para_Diretorio_do_programa()