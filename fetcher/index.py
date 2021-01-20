
import csv
from registration import register

def fetch(email):
    print(f'Fetching {email}')
    with open('data.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        header = next(spamreader)
        for row in spamreader:
            print(row)
            data = {}
            data['email'] = row[0]
            data['password'] = row[1]
            print(data)
            register(data['email'], data['password'])