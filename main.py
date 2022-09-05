from selenium import webdriver


def get_driver():
    # set options to make browsing easier
    #empty class call without an argument
    options = webdriver.ChromeOptions()
    # in options we add argument, these flags as options. These are bars that show memory is low, etc these bars can interfere / confuse cursor
    options.add_argument("disable-infobars")
    #start browser maximized
    options.add_argument("start-maximized")
    #avoid issues occure in linux computers, repl is linux
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("disable-infobars")
    #browsers sometimes use sandboxes so disable it to scrape
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    #Main driver - options have all the have arguments
    #name of the argument = variables
    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value = "/html/body/div[1]/div/h1[1]")
    return element.text


print(main())
