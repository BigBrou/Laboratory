from selenium import webdriver

url = "https://google.com"

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)
browser.get(url)
r = browser.execute_script("return 100+50")
print(r)
