import requests
import json

"""
    To get the access token goto http://graph.facebook.com/tools/explorer
    With "Get Access Token" option select "user_group" and "Friend_group" in "User Data Permissions" and "Friends Data Permissions"
"""
TOKEN = '' 

#Collects all group names and group id from the user which he belongs to
def get_groups():
    
    query = ("SELECT gid,name FROM group where gid in ( SELECT gid FROM group_member WHERE uid=me())")
    payload = {'q':query,'access_token': TOKEN}
    response = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(response.text)
    return result['data']

#Post feeds to all the groups
def Post_status(name):
    message=raw_input("Enter your message to be posted:")
    for i in name:
        try:
            check=raw_input("Want to post in %s?(Y/N)" % i['name'])
        except UnicodeError:
            continue
        if check=='N':
            continue
        post_data = {'access_token':TOKEN, 'message':message}
        url='https://graph.facebook.com/%s/feed' % str(i['gid'])
        response = requests.post(url,data=post_data)
        
if __name__ == '__main__':
    Post_status(get_groups())
    
#To run the script "python group_post.py"
    
