from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Configurações do Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # roda sem abrir a janela
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Caminho para o seu chromedriver
service = Service('C:/Users/Leoda/OneDrive/Documentos/vscode/python/POO/Desafio/chromedriver.exe')

# Inicializa o navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL alvo
url = 'https://www.mascus.com/+/itemtype=usedad/1,relevance,search.html'
driver.get(url)

# Espera a página carregar completamente
time.sleep(5)

# Lista para guardar os dados
data = []

# Captura o bloco das categorias
try:
    categories_block = driver.find_element(By.ID, 'searchFacet_Category')
    main_categories = categories_block.find_elements(By.CSS_SELECTOR, 'li')

    for main_cat in main_categories:
        try:
            inventory_type = main_cat.find_element(By.TAG_NAME, 'span').text.strip()

            # Clica para abrir subcategorias se necessário
            expand_button = main_cat.find_element(By.CLASS_NAME, 'facet__expand-icon')
            driver.execute_script("arguments[0].click();", expand_button)
            time.sleep(1)

            subcat_list = main_cat.find_elements(By.CSS_SELECTOR, 'ul li')

            for subcat in subcat_list:
                try:
                    category = subcat.find_element(By.TAG_NAME, 'span').text.strip()

                    # Captura sub-subcategorias se tiver
                    try:
                        expand_button2 = subcat.find_element(By.CLASS_NAME, 'facet__expand-icon')
                        driver.execute_script("arguments[0].click();", expand_button2)
                        time.sleep(1)

                        subsub_list = subcat.find_elements(By.CSS_SELECTOR, 'ul li')

                        for subsub in subsub_list:
                            subcategory = subsub.find_element(By.TAG_NAME, 'span').text.strip()
                            data.append([inventory_type, category, subcategory, '', '', '', ''])

                    except:
                        # Se não tiver sub-subcategoria
                        data.append([inventory_type, category, '', '', '', '', ''])

                except Exception as e:
                    print(f"Erro ao capturar subcategoria: {e}")

        except Exception as e:
            print(f"Erro ao capturar categoria principal: {e}")

except Exception as e:
    print(f"Erro ao encontrar bloco de categorias: {e}")

# Captura filtros de Make, Model, Continent, Country se existirem
try:
    # Faz uma pesquisa simulada para ativar filtros
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[class*="searchbutton"]')
    driver.execute_script("arguments[0].click();", search_button)
    time.sleep(5)

    # Agora captura os filtros
    try:
        make_block = driver.find_element(By.ID, 'searchFacet_Make')
        makes = make_block.find_elements(By.CSS_SELECTOR, 'li')
        make_list = [make.find_element(By.TAG_NAME, 'span').text.strip() for make in makes]
    except:
        make_list = []

    try:
        model_block = driver.find_element(By.ID, 'searchFacet_ModelGroup')
        models = model_block.find_elements(By.CSS_SELECTOR, 'li')
        model_list = [model.find_element(By.TAG_NAME, 'span').text.strip() for model in models]
    except:
        model_list = []

    try:
        continent_block = driver.find_element(By.ID, 'searchFacet_Continent')
        continents = continent_block.find_elements(By.CSS_SELECTOR, 'li')
        continent_list = [continent.find_element(By.TAG_NAME, 'span').text.strip() for continent in continents]
    except:
        continent_list = []

    try:
        country_block = driver.find_element(By.ID, 'searchFacet_Country')
        countries = country_block.find_elements(By.CSS_SELECTOR, 'li')
        country_list = [country.find_element(By.TAG_NAME, 'span').text.strip() for country in countries]
    except:
        country_list = []

except Exception as e:
    print(f"Erro ao capturar filtros: {e}")

# Fecha o navegador
driver.quit()

# Monta o dataframe
df = pd.DataFrame(data, columns=["Inventory Type", "Category", "Subcategory", "Make", "Model", "Continent", "Country"])

# Preenche as colunas de Make, Model, Continent e Country como listas separadas
if data:
    # Só preenche se forem encontrados
    if make_list:
        df['Make'] = ', '.join(make_list)
    if model_list:
        df['Model'] = ', '.join(model_list)
    if continent_list:
        df['Continent'] = ', '.join(continent_list)
    if country_list:
        df['Country'] = ', '.join(country_list)

# Salva no CSV
df.to_csv('mascus_categories.csv', index=False, encoding='utf-8-sig')

print("Arquivo mascus_categories.csv gerado com sucesso!")
