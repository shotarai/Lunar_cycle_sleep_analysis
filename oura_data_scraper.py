import os
import csv
import sys
import time
import glob
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from faulthandler import is_enabled

# コマンド入力処理
want_data = sys.argv
data_label = ['sleep','daily-sleep','daily-readiness','daily-activity','notes-tags','heart-rate','bedtime','smoothed-location']
if len(want_data) == 9:
    bool_data = [int(x) for x in want_data[1:]]
    data_label = [data_label[x] for x in range(len(data_label)) if bool_data[x] == 1]

with open('oura_users.csv', newline='', encoding='utf-8') as csvfile:
# csv.readerでファイルを読み込む
    reader = csv.reader(csvfile)
# データをリストに保存
    data = [row for row in reader]

# ChromeOptionsオブジェクトの作成
options = webdriver.ChromeOptions()

# ダウンロードフォルダの指定
download_dir = os.path.abspath(os.path.dirname(__file__)) + "/oura_user"
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
url = 'https://cloud.ouraring.com/'
driver.get(url)

#csvファイルをダウンロードしにいく関数
def login_to_get_csvs(login_data, label):
    while True:
        try:
            #メアドパスワード入力
            login_id = login_data[0].replace('\ufeff', '')
            login_pw = login_data[1].replace('\ufeff', '')
            input_id = driver.find_element(By.ID,"email")
            input_id.clear()
            input_password = driver.find_element(By.ID,"password")
            input_password.clear()
            input_id.send_keys(login_id)
            input_password.send_keys(login_pw)
        except:
            print('continue!')
            continue
        break


    j = 0
    #ログインボタンを押す
    while True:
        try:
            button_login = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/main/div/form/div[3]/button')
            button_login.click()
        except:
            if j < 4:
                print('continue!')
                j += 1
                continue
            else:
                return
        break
    j = 0
    #データ取得画面に遷移
    while True:
        try:
            button_back = driver.find_element(By.ID,'menu-button--menu')
            button_back.click()
            button_back = driver.find_element(By.ID,"option-0--menu--1")
            button_back.click()
        except:
            if j < 12:
                time.sleep(5)
                print('continue!')
                j += 1
                continue
            else:
                return
        break

    for name in label:
        while True:
            try:
                # ダウンロードリンクをクリック
                data_pass = '//a[@href="/account/export/' + name + '/csv"]'
                download_link = driver.find_element(By.XPATH, data_pass)
                download_link.click()

                # ダウンロード完了を待つ
                time.sleep(10)

                # ファイル名を変更
                all_files = glob.glob(os.path.join(download_dir, "*"))

                # 最も最近更新されたファイルを取得する
                latest_file = max(all_files, key=os.path.getctime)

                # ファイル名を変更する
                new_file_name = login_pw + '_' + name + ".csv"
                os.rename(latest_file, os.path.join(download_dir, new_file_name))
            except:
                print('continue!')
                continue
            break
    # サインイン画面に戻る
    while True:
        try:
            button_back = driver.find_element(By.ID,'menu-button--menu')
            button_back.click()
            button_back = driver.find_element(By.ID,"option-1--menu--1")
            button_back.click()
        except:
            print('continue!')
            continue
        break    

#全ての参加者で回す
for proton in data:
    time.sleep(5)
    login_to_get_csvs(proton, data_label)

driver.close()