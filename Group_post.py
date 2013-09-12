import requests
import json
import urllib
import urllib2

"""
    To get the access token goto http://graph.facebook.com/tools/explorer
    With "Get Access Token" option select "user_group" and "Friend_group" in "User Data Permissions" and "Friends Data Permissions"
"""
TOKEN = '<access_token'

#Collects all group names and group id from the user which he belongs to
def get_groups():
    
    query = ("SELECT gid,name FROM group where gid in ( SELECT gid FROM group_member WHERE uid=me())")
    payload = {'q':query,'access_token': TOKEN}
    response = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(response.text)
    return result['data']
    

#Post feeds to all the groups
def Post_status(name):
    for i in name:
        post_data = {'access_token':TOKEN, 'message':'<content>'}
        request_path = str(i['gid'])+'/feed'
        post_data = urllib.urlencode(post_data)
        response = urllib2.urlopen('https://graph.facebook.com/%s' % request_path, post_data)

if __name__ == '__main__':
    Post_status(get_groups())
    
#To run the script "python group_post.py"
