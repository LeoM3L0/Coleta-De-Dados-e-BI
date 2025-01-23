from selenium import webdriver
from selenium.webdriver.common.by import By
from alive_progress import alive_bar
from time import sleep

# periodo = input('Pesquisar por periodo? [S] ou [N]\n').upper()
# inicio = '01/{}/{}'.format(date.month, date.year)
# fim = '30/{}/{}'.format(date.month, date.year)

# if periodo == "S":
#     inicio = input("Digite o data inicial (no formato dd/mm/yyyy): ")
#     fim = input("Digite o data final (no formato dd/mm/yyyy): ")
    
# else:
#     print('Continuando procedimento pré-programado (Capturando apenas o dia atual!)')
    
url = 'https://guiaodonto.com/home/dash' 

options = webdriver.ChromeOptions() 
options.add_argument("--headless=new")

print("CARREGANDO PAGINA: ")
with alive_bar(5) as bar:
    for i in range(5):
        sleep(0.7)
        bar()
        
driver = webdriver.Chrome(options=options)
driver.get(url) 

driver.implicitly_wait(0.5) 

elemento_login = driver.find_element(by=By.XPATH, value='//*[@id="login_logar"]') 
elemento_senha = driver.find_element(by=By.XPATH, value='//*[@id="senha_logar"]') 

login = "" 
senha = "" 

elemento_login.send_keys(login) 
elemento_senha.send_keys(senha) 

elemento_login.submit() 
driver.implicitly_wait(1) 

original_window = driver.current_window_handle
