Facebook-Scripts
================

Playing around with Graph API using python

This script is used to update selected Facebook groups of the user with any specific message. We use Graph API provided by Facebook for the same.
To use the Graph API, it is necessary for the user to generate an Access Token. 

The script depends on the following packages:

1) requests module. Do check this page for installing requests module (http://docs.python-requests.org/en/latest/user/install/)

Steps to use the Access Token in the script:

1) Go to the following page, https://developers.facebook.com/tools/explorer/

2) Login with your regular Facebook ID.

3) In the Access Token Edit Box, you might see some existing token already. Press "x" near the Edit Box to clear the Access Token.

4) Now select "Get Access Token" to get a new Access Token.

5) In the "Select Permissions" pop-up, under "User Data Permissions" tab, select "user_group" and in "Friends Data Permissions" tab, 
select "Friends_groups".

6) Click "Get Access Token".

7) In The Access Token Edit Box, you will now see the Access Token generated with new permissions.


How to use the script:

1) Once you have generated the access token, please edit the script, group_post.py and add the access token in the line:
TOKEN="";

2) Now run the script from the command line. 

3) The script will ask to input the message that you want to post in different groups. The current script only supports single post to all the groups.

4) After this, the script will go through all the groups that you are part of and ask you if you want to post in them one by one.

5) Script will end after it has iterated over all the groups.
