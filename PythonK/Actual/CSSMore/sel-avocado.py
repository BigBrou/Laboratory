from bs4 import BeautifulSoup
import sys
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), "utf-8")


corepath = os.getcwd()
path = os.path.join(corepath, "Actual\\CSSMore\\fruits-vegetables.html")
print(path)

fp = open(path, encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

texting = lambda q : print(soup.select(q).string)

#texting("#main-goods > ul#ve-list > li:nth-of-type(4)")

cond = {"data-lo" : "us", "class" : "black"}
print(soup.find("li", cond).string)
print(soup.find(id='ve-list').find("li", cond).string)
