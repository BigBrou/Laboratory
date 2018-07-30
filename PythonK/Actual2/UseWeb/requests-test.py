import requests

r = requests.get("http://api.aoikujira.com/time/get.php")
text = r.text
bin = r.content

print(text)
print(bin)
