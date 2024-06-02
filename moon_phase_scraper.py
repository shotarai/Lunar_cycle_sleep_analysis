import os
import csv
import time
import glob
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from faulthandler import is_enabled

# ChromeOptionsオブジェクトの作成
options = webdriver.ChromeOptions()

# ダウンロードフォルダの指定
download_dir = os.path.abspath(os.path.dirname(__file__)) + "/moon"
prefs = {'download.default_directory': download_dir}
options.add_experimental_option('prefs', prefs)

# ダウンロード時のポップアップを無効にする
options.add_experimental_option("excludeSwitches",['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')


# ChromeのWebDriverオブジェクトを作成する
driver = webdriver.Chrome(os.path.abspath(os.path.dirname(__file__)) + '/chromedriver',chrome_options=options)


element = WebDriverWait(driver, 30)

# ダウンロードしたいリンクを開く
url = 'https://eco.mtk.nao.ac.jp/cgi-bin/koyomi/koyomiy.cgi'
driver.get(url)

#地域の登録
while True:
    try:
        button_region = driver.find_element(By.ID,'NAO_id')
        button_region.click()
    except:
            print('continue!')
            continue
    break

#大阪に変更
while True:
    try:
        button_back = driver.find_element(By.XPATH,'//*[@id="NAO_id"]/optgroup[5]/option[4]')
        button_back.click()
    except:
            print('continue!')
            continue
    break

#一年間のデータ取得
while True:
    try:
        button_back = driver.find_element(By.XPATH,'//*[@id="menu"]/div[1]/fieldset[4]/div[5]/input')
        button_back.click()
    except:
            print('continue!')
            continue
    break

df = pd.DataFrame()

for age in [2021, 2022, 2023]:

     #年数の指定
    while True:
        try:
            input_age = driver.find_element(By.ID,"year")
            input_age.clear()
            input_age.send_keys(age)
        except:
            print('continue!')
            continue
        break

    #実行
    while True:
        try:
            button_back = driver.find_element(By.XPATH,'//*[@id="tdleft"]/tbody/tr[6]/td[2]/input')
            button_back.click()
        except:
            print('continue!')
            continue
        break

    if driver.find_element(By.CLASS_NAME,"result").is_enabled:
        info = driver.find_element(By.CLASS_NAME,"result").text
        if info:
            tmp = info.split()
            result1 = []
            result2 = []
            for i in range((len(tmp)//7) - 1):
                result1.append(tmp[12 + 7*i])
                result2.append(tmp[7 + 7*i])
            old_df = pd.DataFrame({'day': result2, 'moon_phase': result1}) 
            df = pd.concat([df, old_df], ignore_index=True)

df.to_csv('moon_info.csv', index=False)
driver.close()