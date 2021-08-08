# pip install selenium
# pip install webdriver-manager
# import Required Libraries


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

search = str(input('Enter your search: '))

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(2)

final_search = f'https://www.google.com/search?q={search}'
driver.get(final_search)
