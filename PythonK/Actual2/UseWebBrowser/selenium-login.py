from selenium import webdriver
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

USER = "kangchoi21"
PASS = "rattle21!"

browser = webdriver.PhantomJS()
browser.implicitly_wait(5)

url_login = "https://www.ubware.com/Member/Logon"
browser.get(url_login)
print("로그인 페이지에 접근")

e = browser.find_element_by_id("txtID")
e.clear()
e.send_keys(USER)

e = browser.find_element_by_id("txtPassword")
e.clear()
e.send_keys(PASS)

form = browser.find_element_by_css_selector("input.btnSubmit[type=fctSaveCookie]")
form.submit()
print("로그인 페이지 클릭함")

products = browser.find_elements_by_css_selector("viewLastes.tr")
print(products)
for product in products:
    print("-", product.text)
