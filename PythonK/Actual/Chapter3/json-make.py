import json

price = {
    "date"  : "2018-06-01",
    "price" : {
        "Apple"  : 80,
        "Orange" : 55,
        "Banana" : 40
    }
}

s = json.dumps(price)
print(s)
