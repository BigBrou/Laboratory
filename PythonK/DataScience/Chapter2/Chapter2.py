import re

my_regex = re.compile("[0..9]+", re.I)

def apply_to_one(f):
    return f(2)

y = apply_to_one(lambda x: x + 4)
print(y)


#another_double = lambda x: x * 2 ???
def another_double(x):
    return x * 2

grade = {"joel" : 80, "Tim" : 95}
grade["back"] = 70
print (grade)

joel_has_grade = "joel" in grade
print(joel_has_grade)

joels_grade = grade.get("joel", 0)
print(joels_grade)

no_one = grade.get("no") #default is None
print(grade)
print(no_one)

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome"]
}
print (tweet)

document = ('Return the value for key if key is in the dictionary, else default. If default is not given,'+
            'it defaults to None, so that this method never raises a KeyError')
print(type(document))
######
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print('$$$$$$$$$$$$$$$$$$$$$$')
print(word_counts)
#wc = sorted(word_counts.items(), key=lambda (word, count): count, reverse = True)
#print(wc)

word_counts2 = {}
for word in document:
    try:
        word_counts2[word] += 1
    except:
        word_counts2[word] = 1

word_counts3 = {}
for word in document:
    previous_count = word_counts3.get(word, 0)
    word_counts3[word] = previous_count + 1

###################################################
#defaultDict
from collections import defaultdict

word_counts_int = defaultdict(int)
for word in document:
    word_counts_int[word] += 1
word_counts_int = sorted(word_counts_int.items())
print(word_counts_int)

word_counts_list = defaultdict(list)
word_counts_dict = defaultdict(dict)
word_counts_dict["Joel"]["City"] = "Seattle"
print(word_counts_dict)
##################################################
#Counter
from collections import Counter
c = Counter([0, 1, 2, 0])
print(c)

##################################################
# sort
x = [4, 1, 2, 3]
print(x)
y = sorted(x)
x.sort()
print(x)
print(y)

x = [-4, 1, -2, 3]
y = sorted(x, key=abs, reverse=False)
print(y)

#lambda
x = 1
y = lambda x: x + 4
print()
