from click import option
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class Cephali():
    def solve(site_key):
        options = Options()
        #options.add_argument("--headless")
        driver = webdriver.Chrome(options=options,executable_path=ChromeDriverManager().install())
        time.sleep(2)
        driver.get("http://localhost:5000/api/captcha/solve/"+site_key)
        driver.find_elements_by_tag_name("iframe")[0].click()
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((driver.find_elements_by_tag_name("iframe")[0])))
        time.sleep(5)
        print(driver.find_elements_by_tag_name("button"))
        driver.find_element_by_xpath('//*[@id="recaptcha-audio-button"]').click()
        #driver.quit()

        return str(driver.find_elements_by_tag_name("button"))