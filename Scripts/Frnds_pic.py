import requests
import json

TOKEN = '<access_token>'


def get_data():
    query = ('SELECT first_name,sex,pic_big FROM user WHERE uid in (SELECT uid2 FROM friend WHERE uid1 = me())')
    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']


def Download_pics(xs):
    choice = raw_input("Download Options:\n1.All\n2.Specific\nSex\n\t3.Male\n\t4.Female\n\nEnter Your Choice: ")
    if choice == '1':
        for x in xs:
            r = requests.get(x['pic_big'], stream=True)
            file = open(x['first_name'] + '.jpg', 'wb')
            for block in r.iter_content(1024):
                file.write(block)
            print
            "Successfully Downloaded %s" % x['first_name']
    elif choice == '3':
        for x in xs:
            if x['sex'] == 'male':
                r = requests.get(x['pic_big'], stream=True)
                file = open(x['first_name'] + '.jpg', 'wb')
                for block in r.iter_content(1024):
                    file.write(block)
                print
                "Successfully Downloaded %s" % x['first_name']
    elif choice == '4':
        for x in xs:
            if x['sex'] == 'female':
                r = requests.get(x['pic_big'], stream=True)
                file = open(x['first_name'] + '.jpg', 'wb')
                for block in r.iter_content(1024):
                    file.write(block)
                print
                "Successfully Downloaded %s" % x['first_name']

    else:
        for x in xs:
            msg = 'Do you want to download %s Profile pic?(Y/N)' % x['first_name']
            spec = raw_input(msg)
            if spec == 'Y':
                r = requests.get(x['pic_big'], stream=True)
                file = open(x['first_name'] + '.jpg', 'wb')
                for block in r.iter_content(1024):
                    file.write(block)
                print
                "Successfully Downloaded %s" % x['first_name']


if __name__ == '__main__':
    Download_pics(get_data())
