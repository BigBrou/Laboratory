#List iof Dictionaries
users = [
    {'id': 0, 'name': 'Hero'},
    {'id': 1, 'name': 'Dunn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chi'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Devin'},
    {'id': 8, 'name': 'Kate'},
    {'id': 9, 'name': 'Klein'}
]

#List of Tuples
friendShip = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
              (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

#for i, j in friendShip:
#    users[i]["friends"].append(users[j])  #j를 i 친구로 추가
#    users[j]["friends"].append(users[i])  #i를 j 친구로 추가

for i, j in friendShip:
    users[i]["friends"].append(users[j])  #j를 i 친구로 추가
    users[j]["friends"].append(users[i])  #i를 j 친구로 추가

def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user)
                        for user in users)

print(total_connections)

#for user in users:
#    print(user)

#from__future__import division
num_users = len(users)
avg_connections = total_connections/ num_users
print(avg_connections)

def friends_of_friend_ids_bad(user):
    return [foaf["id"]
            for friend in user["friends"] # for each of user's friends
            for foaf in friend["friends"]] # get each of _their_ friends
