from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <div id="meigen">
                <h1>Books</h1>
                <ul class="items">
                    <li>unity games</li>
                    <li>swift starts</li>
                    <li>modern web site</li>
                </ul>
            </div>
        </body>
    </html>
"""

soup = BeautifulSoup(html, "html.parser")

h1 = soup.select_one("div#meigen > h1").string
print("h1 =", h1)

li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
    print("li =", li.string)
