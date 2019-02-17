import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json
# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def file_acess():
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    info = json.loads(data)
    info = info[0]
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    while True:
        for el in info.keys():
            print(el)
        print('*'*100)
        next_step = input("where to move forward(type\
                                nowhere if you want to stop on this file): ")
        print('*'*100)

        if next_step == 'nowhere':
            return info

        if type(info[next_step]) == dict:
            info = info[next_step]

        else:
            print("Endpoint of the file")
            return info[next_step]

if __name__ == '__main__':
    TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    acct = input('Enter Twitter Account:')
    print(file_acess())



