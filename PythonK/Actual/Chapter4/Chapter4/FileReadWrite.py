f = open("write.txt", 'w')
for i in range(1, 11):
    f.write(str(i))
f.close()

f = open("write.txt", 'r')
line = f.readline()
print(line)
f.close()


#Quiz 3
