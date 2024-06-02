import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from faulthandler import is_enabled

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",['enable-automation'])
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=options)

with open('oura_users.csv', newline='', encoding='utf-8') as csvfile:
# csv.readerでファイルを読み込む
    reader = csv.reader(csvfile)
# データをリストに保存
    data = [row for row in reader]

element = WebDriverWait(driver, 30)

# ダウンロードしたいリンクを開く
url = 'https://cloud.ouraring.com/'
driver.get(url)

def login_to_time_records(proton):
    login_id = proton[0].replace('\ufeff', '')
    login_pw = proton[1].replace('\ufeff', '')
    input_id = driver.find_element(By.ID,"email")
    input_id.clear()
    input_password = driver.find_element(By.ID,"password")
    input_password.clear()

    input_id.send_keys(login_id)
    input_password.send_keys(login_pw)

    button_login = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/main/div/form/div[3]/button')
    button_login.click()

    time.sleep(10)

    time.sleep(7)
    while True:
        try:
            button_back = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div/main/div/div[1]/div[1]/div[1]/button[1]')
            button_back.click()
            graph = driver.find_element(By.CLASS_NAME,'phases')
            actions = ActionChains(driver)
            actions.move_to_element(graph)
            actions.move_by_offset(-((graph.rect['width']-1) // 2),0)
            actions.perform()
            graph_width = graph.rect['width']
        except:
            print('continue!')
            continue

        break

    record = {}
    time.sleep(7)

    for i in range(int(graph_width)):
        if driver.find_element(By.CLASS_NAME,"hover").is_enabled:
            info = driver.find_element(By.CLASS_NAME,"hover").text
            if not info:
                continue
            tmp = info.split()
            record[tmp[0]] = tmp[2]

        actions = ActionChains(driver)
        actions.move_by_offset(1,0)
        actions.perform()
    time.sleep(7)
    button_back = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div/main/div/div[1]/div[1]/div[1]/button[1]')
    button_back.click()
    print(record)




#全ての参加者で回す
for proton in data:
    time.sleep(5)
    login_to_time_records()(proton)

driver.close()
