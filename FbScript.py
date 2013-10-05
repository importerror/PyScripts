
import requests
import json
import sys

'''
    To get the access token goto http://graph.facebook.com/tools/explorer

'''

TOKEN = '<access token>'

# Collects data and send it to the respective function

Group_post = "SELECT gid,name FROM group where gid in ( SELECT gid FROM group_member WHERE uid=me())"


def get_data(fql):

    query = (fql)
    payload = {'q': query, 'access_token': TOKEN}
    response = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(response.text)
    return result['data']

# Post feeds to all the groups


def post_status(name):
    message = raw_input("Enter your message to be posted:")
    for i in name:
        try:
            prompt = u"Want to post in %s?(Y/N) " % i['name']
            check = raw_input(prompt.encode(sys.stdout.encoding))
        except UnicodeError:
            continue
        if (check == 'N') | (check == 'n'):
            continue
        post_data = {'access_token': TOKEN, 'message': message}
        url = 'https://graph.facebook.com/%s/feed' % str(i['gid'])
        response = requests.post(url, data=post_data)
        print "Successfully posted in %s" % i['name']

if __name__ == '__main__':
    action = raw_input("Menu\n1.Group Post\n\nEnter Your Choice: ")
    if action == '1':
        post_status(get_data(Group_post))

# To run the script "python gFbScript.py"
