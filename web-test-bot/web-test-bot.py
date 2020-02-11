from selenium import webdriver

def lambda_handler(event, context)

    driver = webdriver.chrome('./chromedriver')

    driver.get('https://www.naver.com')
    driver.implicitly_wait(3)
    driver.get_screenshot_as_file('capture.png')
    driver.quit()

    return {
        'statusCode': 200
    }