# Este script é apenas para fins educacionais, demonstrando a automação web com Selenium.
# Por favor, use-o de forma responsável e em conformidade com os Termos de Serviço do LinkedIn.
# O uso indevido de ferramentas de automação pode levar a restrições de conta ou outros problemas.
# O autor não se responsabiliza por qualquer uso indevido.

import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

# Carrega os cookies do arquivo cookies.json
# Este arquivo deve conter os cookies exportados de uma sessão logada do LinkedIn.
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

# Configura o serviço do ChromeDriver para gerenciar automaticamente o driver do Chrome.
# Isso garante que a versão correta do ChromeDriver seja usada com o seu navegador Chrome.
service = ChromeService(ChromeDriverManager().install())

# Inicializa o driver do Chrome, que controlará o navegador.
driver = webdriver.Chrome(service=service)

# Navega para o domínio do LinkedIn para que os cookies possam ser adicionados corretamente.
# Os cookies só podem ser adicionados para o domínio atual.
driver.get("https://www.linkedin.com/")

# Adiciona os cookies carregados ao navegador.
# Isso permite que a sessão do usuário seja restaurada sem a necessidade de login manual.
for cookie in cookies:
    # O atributo 'sameSite' pode causar problemas se não for um dos valores esperados pelo Selenium.
    # Removemos ele se for um valor inválido para evitar erros.
    if 'sameSite' in cookie and cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
        del cookie['sameSite']
    try:
        driver.add_cookie(cookie)
    except WebDriverException as e:
        print(f"Erro ao adicionar cookie: {cookie}\n{e}")


# Navega para a página inicial do LinkedIn para verificar se o login foi bem-sucedido.
# Se os cookies foram adicionados corretamente, o usuário deve estar logado.
driver.get("https://www.linkedin.com/feed/")

print("O script continuará em 5 segundos.")
time.sleep(5)

print("Continuando a execução...")

# Define o número de conexões a serem enviadas.
# Este valor pode ser ajustado para controlar a quantidade de solicitações de conexão.
num_connections_to_send = 3 # Você pode alterar este valor

# Navega para a página "Minha Rede" do LinkedIn, onde as sugestões de conexão são exibidas.
print("Navegando para a página 'Minha Rede'...")
driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(5) # Espera a página carregar completamente para garantir que os elementos estejam disponíveis.

# Loop para encontrar e clicar nos botões "Conectar" até que o número desejado de conexões seja enviado.
connections_sent = 0
while connections_sent < num_connections_to_send:
    try:
        print(f"Procurando botões 'Conectar' (conexões enviadas: {connections_sent}/{num_connections_to_send})...")
        # Encontra todos os botões "Conectar" visíveis na página.
        # O seletor CSS busca por botões com um atributo 'aria-label' que começa com "Convidar".
        connect_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[aria-label^="Convidar"]')

        if not connect_buttons:
            print("Nenhum botão 'Conectar' encontrado na página. Encerrando o processo de conexão.")
            break # Sai do loop se não houver mais botões para clicar.

        # Clica no primeiro botão "Conectar" encontrado.
        connect_button = connect_buttons[0]
        print(f"Botão encontrado. Clicando... (Conexão {connections_sent + 1}/{num_connections_to_send})")
        connect_button.click()
        print("Clicado com sucesso.")
        connections_sent += 1

        # Se ainda houver conexões a serem enviadas, aguarda um tempo antes da próxima tentativa.
        # Isso ajuda a simular um comportamento humano e evitar detecção por automação.
        if connections_sent < num_connections_to_send:
            print("Aguardando 5 segundos antes da próxima conexão para evitar Rate limit...")
            time.sleep(5) # Delay entre as conexões
        else:
            print("Número de conexões desejado atingido. Processo de conexão concluído.")

    except Exception as e:
        print(f"Erro ao tentar clicar no botão 'Conectar': {e}. Isso pode ocorrer se a página mudar ou se não houver mais botões visíveis. Encerrando o processo de conexão.")
        break # Sai do loop em caso de erro inesperado.

print("Processo de automação de conexão finalizado.")
time.sleep(10) # Mantém o navegador aberto por um tempo para inspeção final do usuário.

# Fecha o navegador.
driver.quit()
# Legal, né?