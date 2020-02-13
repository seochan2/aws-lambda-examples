from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def lambda_handler(event, context)
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('windows-size=1920x1080')
    options.add_argument('disable-gpu')
    
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser':'ALL'}
    
    driver = webdriver.chrome('./chromedriver', options=options, desired_capabilities=d)

    driver.get('https://www.naver.com')
    driver.implicitly_wait(3)
    driver.get_screenshot_as_file('capture.png')
    driver.quit()

    return {
        'statusCode': 200
    }