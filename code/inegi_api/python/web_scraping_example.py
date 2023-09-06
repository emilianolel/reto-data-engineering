from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


# writes an html file form the url in the path
def get_html_file(url, path):

    url_nbr_page = url[-2:]

    # Instance of webdriver
    driver = webdriver.Firefox(options=options)

    driver.get(url)

    raw_title = driver.title

    page_title = raw_title.replace('|', '').replace(' ', '_').replace('__', '-').lower()

    file_name = page_title + '_' + url_nbr_page + '.html'

    print(f'--> Procesing file: {file_name}')

    complete_file_path = path + file_name

    with open(file=complete_file_path, mode='w') as f:

        print(driver.page_source, file=f)



# Seleniun Options
options = Options()
options.add_argument('-headless')
options.add_argument("--window-size=1920,1200")


path = 'data/lake/'


for page in range(1, 10):

    url = f'https://www.vivanuncios.com.mx/s-renta-inmuebles/nuevo-leon/page-{page}/v1c1098l1018p{page}'

    get_html_file(url=url, path=path)

    time.sleep(10)

