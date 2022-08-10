import csv
# import UserHandler
# UH = UserHandler

def find_index(input):
    global row
    fl = open('UserList.csv', 'r').readlines()
    for row in fl:
        if row.startswith(input):
            print(row)
find_index('tassos')






for i in row:
    if int(i.isnumeric()):
        print(i)