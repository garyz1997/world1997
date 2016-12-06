#!/usr/bin/python
print 'Content-type: text/html\n\n'
import cgi, cgitb, os, time
cgitb.enable()

j = open('../data/loggedin.txt','r')
userData = j.readlines()
j.close()
users = []
for line in userData:
    users.append(line.strip('\n').split(','))

#check user sequence
activeUser = ''
date = time.strftime("%Y%m%d")
for user in users:
    if cgi.escape(os.environ["REMOTE_ADDR"]) == user[2]:
        activeUser = user[0]
        
j=open('../data/loggedin.txt', 'r')
number=j.read()
j.close()
lines=[]
x = 0
userNum = 0
date = time.strftime("%Y%m%d")
for line in number.split('\n'):
    lines.append(line.split(','))
    if activeUser == line.split(',')[0]:
        userNum = x
    x+=1

for user in range(len(lines)-1):
    if lines[user][3] != date:
        lines[user][1] = '0'
lines[userNum][1] = '0'
s=open('../data/loggedin.txt', 'w')
for line in range(len(lines)):
    lines[line] = ','.join(lines[line])
number = '\n'.join(lines)
s.write(number)
s.close()
    
print'''
<!DOCTYPE html>
<html>

<head>
   <title>
      Data
   </title>
   <link href="//d2nqa8qx64ku3x.cloudfront.net/assets/landing-new-0ec07127ff697c975eef30ccf6decd3f.css" media="screen" rel="stylesheet" type="text/css" />
<link href="layout.css" media="screen" rel="stylesheet" type="text/css" />
<link href="bg.css" media="screen" rel="stylesheet" type="text/css" />
</head>

<body>

<div class='terms-overlay'>
<div class='terms-container'>
<div class='terms-close'>&times;</div>
<div class='terms-title'></div>
<div class='terms-content'></div>
<div class='terms-ok-button btn'>OK</div>
</div>
</div>
<div class='sections'>
<div class='section dark resize selected see-more-section'>
<div class='inner fade'>
<div class='container center fixed-container'>
<div class='clearfix'>
<div class='sixteen columns'>
<div class='tagline-line'></div>

<h3 class='tagline'>You have logged out successfully. </h3>
<a href="login.html">Back to the main page</a>

</div></div></div></div></div></div></div></div>
<!--Made by Derek-->
</body>
</html>'''

