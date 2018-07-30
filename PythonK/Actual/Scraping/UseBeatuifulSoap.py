from bs4 import BeautifulSoup

#HTML Use
html = """
    <html>
        <body>
            <h1 id="title">What is Scraping ? </h1>
            <p id="body">Web Page</p>
            <p>Extract what i want</p>
        </body>
    </html>
"""

soup = BeautifulSoup(html, 'html.parser')

#p1 = soup.html.body.p
#h1 = soup.html.body.h1
#p2 = p1.next_sibling.next_sibling

#print("h1 = " + h1.string)
#print("p = " + p1.string)
#print("p = " + p2.string)

title = soup.find(id="title")
body = soup.find(id="body`")

print("#title = "+title.string)
print("body = "+body.string)
