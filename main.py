from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

store_names = []
addresses = []
result_text = ""
driver = webdriver.Chrome()



for i in range(10):
    try:
        driver.get(f"https://www.aeon.com/store/list/ショッピングセンター/関東地方/p_{i+1}/")
        #driver.get("https://www.aeon.com/store/list/総合スーパー/イオン・イオンスタイル/関東地方/東京都/")
        store_elems = driver.find_elements(By.CLASS_NAME, "storeName")
        address_elems = driver.find_elements(By.CLASS_NAME, "address")
        adds_elem = driver.find_elements(By.CLASS_NAME, "adds")
        plus_num = 0
        plus_num2 = 0
        for s in range(20):
        #    if len(adds_elem)!=0 and adds_elem[s].text.isspace():
        #        store_name = store_elems[s].text
        #        store_names.append(store_name)
        #        addresses.append('')
        #        print(store_names)
        #        print(addresses)
        #        print(len(store_names), len(addresses))
        #        plus_num += 1
            #        else:
            try:
                store_name = store_elems[s].text
                address = address_elems[s].text
                store_names.append(store_name)
                addresses.append(address)
                print(store_names)
                print(addresses)
                print(len(store_names), len(addresses))
                #sleep(1)
            except:
                pass
    except:
        pass
"""    for k in range(plus_num):
        if adds_elem[k].text.isspace():
            store_name = store_elems[k].text
            store_names.append(store_name)
            addresses.append('')
            print(store_names)
            print(addresses)
            print(len(store_names), len(addresses))
            plus_num2 += 1
        else:
            store_name = store_elems[k].text
            address = address_elems[k].text
            store_names.append(store_name)
            addresses.append(address)
            print(store_names)
            print(addresses)
            print(len(store_names), len(addresses))
            #sleep(1)
    
    for l in range(plus_num2):
        if adds_elem[l].text.isspace():
            store_name = store_elems[l].text
            store_names.append(store_name)
            addresses.append('')
            print(store_names)
            print(addresses)
            print(len(store_names), len(addresses))
        else:
            store_name = store_elems[l].text
            address = address_elems[l].text
            store_names.append(store_name)
            addresses.append(address)
            print(store_names)
            print(addresses)
            print(len(store_names), len(addresses))
            #sleep(1)


        
for s in range(12):
    if adds_elem[s].text.isspace():
        store_name = store_elems[s].text
        store_names.append(store_name)
        addresses.append('')
        print(store_names)
        print(addresses)
        print(len(store_names), len(addresses))
    else:
        store_name = store_elems[s].text
        address = address_elems[s].text
        store_names.append(store_name)
        addresses.append(address)
        print(store_names)
        print(addresses)
        print(len(store_names), len(addresses))
        #sleep(1)"""

"""
for j in range(plus_num+5):
    if adds_elem[s].text.isspace():
        store_name = store_elems[s].text
        store_names.append(store_name)
        addresses.append('')
        print(store_names)
        print(addresses)
        print(len(store_names), len(addresses))
    else:
        store_name = store_elems[s].text
        address = address_elems[s].text
        store_names.append(store_name)
        addresses.append(address)
        print(store_names)
        print(addresses)
        print(len(store_names), len(addresses))
        #sleep(1)
"""

for t in range(len(store_names)):
    result_text = result_text + store_names[t] + "," + addresses[t] + "\n"


with open('result.csv', 'a') as f:
    f.write(result_text)