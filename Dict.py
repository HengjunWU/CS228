import pickle


database = pickle.load(open('userData/database.p','rb'))

# print("1",database)

userName = raw_input('Please enter your name: ')
if userName in database:
    database[userName]["logins"] += 1
    print('welcome back ' + userName + '.')
    userRecord = database[userName]
    # userRecord = OrderedDict(userRecord)
    # print(userRecord)
    # print("2",database)


else:
    database[userName] = {}
    database[userName]["logins"] = 1
    print('welcome ' + userName + '.')
    userRecord = database[userName]
    # print("user",userRecord)
    # userRecord = OrderedDict(userRecord)
    for i in range(10):
        userRecord[('digit{}attempted').format(i)] = 1
    # print("user",userRecord)
    # print("3",database)
    # pickle.dump(database, open('userData/database.p', 'wb'))

# print("4",database)


pickle.dump(database, open('userData/database.p','wb'))

