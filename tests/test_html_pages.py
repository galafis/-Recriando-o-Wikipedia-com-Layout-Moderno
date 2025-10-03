
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_html_pages():
    # Configurações para o Chrome headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Caminho para o chromedriver (assumindo que está no PATH ou em um local conhecido)
    # service = Service(executable_path='/usr/bin/chromedriver') # Ajuste se necessário
    driver = webdriver.Chrome(options=chrome_options)

    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
    html_files = ['index.html', 'personagens.html', 'batalhas.html', 'cultura.html']

    for filename in html_files:
        file_path = os.path.join(base_path, filename)
        print(f"Testando: {file_path}")
        driver.get(f"file://{file_path}")

        # Verifica se o título da página está presente
        assert driver.title != '', f"Título não encontrado em {filename}"

        # Verifica se o cabeçalho principal está presente
        assert driver.find_element(By.TAG_NAME, 'h1').is_displayed(), f"H1 não encontrado em {filename}"

        # Verifica se a navegação está presente
        assert driver.find_element(By.TAG_NAME, 'nav').is_displayed(), f"Nav não encontrado em {filename}"

        print(f"{filename} carregado e elementos básicos verificados com sucesso.")

    driver.quit()

if __name__ == '__main__':
    test_html_pages()

