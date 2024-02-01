from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

store_names = []
addresses = []
result_text = ""
driver = webdriver.Chrome()

for i in range(29):
    try:
        driver.get(f'https://www.mapion.co.jp/phonebook/M02005CM01/{i+64}.html')
        shop_elems = driver.find_elements(By.TAG_NAME, "a")
        address_elems = driver.find_elements(By.TAG_NAME, "td")

        for s in range(100):
        #    print(shop_elems[s+22].text)
        #    print(address_elems[s*2].text)
            store_names.append(shop_elems[s+20].text)
            addresses.append(address_elems[s*2].text)
        #print(store_names)
        #print(addresses)
        #print(len(store_names))
        #print(len(addresses))

    except:
        print('ann error was happened')


print(store_names)
print(addresses)

print(len(store_names))
print(len(addresses))

for t in range(len(store_names)):
    result_text = result_text + store_names[t] + "," + addresses[t] + "\n"


with open('seven_eleven.csv', 'w') as f:
    f.write(result_text)