import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


browser = webdriver.Chrome()
browser.maximize_window()

time.sleep(100)



youtubeVideoLink = "https://www.youtube.com/watch?v=HFZCmHgJh90"





browser.get(youtubeVideoLink)
time.sleep(2)

browser.execute_script("window.scrollBy(0,100)", "")
time.sleep(1)
browser.execute_script("window.scrollBy(0,10)", "")
time.sleep(2)



noMore = 0

while True:
    likeElements = browser.find_elements(By.CSS_SELECTOR, "ytd-toggle-button-renderer[id='like-button']")
    for item in likeElements:
        try:
            item.click()
        except:
            print("hata")
        time.sleep(0.5)

    if len(likeElements) == 0:
        noMore += 1

    if noMore == 50:
        break

    browser.execute_script("window.scrollBy(0,100)", "")
    time.sleep(2)


print("bitti")



time.sleep(25)
browser.close()
