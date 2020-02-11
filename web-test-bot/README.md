# Web Test Bot
=============

### Build an AWS Lambda deployment package for Web Test Bot with Python3

Install Selenium

    pip3 install selenium -t .
    
Install ChromeDriver

    wget https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip
    
    unzip chromedriver_linux64.zip
    
    rm chromedriver_linux64.zip
    
Install Chrome

    sudo vi /etc/yum.repos.d/google-chrome.repo

    [google-chrome]
    name=google-chrome
    baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
    enabled=1
    gpgcheck=1
    gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub

    sudo yum install -y google-chrome-stable