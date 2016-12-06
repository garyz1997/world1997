#!/usr/bin/python
print 'Content-type: text/html\n\n'
import cgi, cgitb, os, time
cgitb.enable()
import md5
form=cgi.FieldStorage()
D={}
for keys in form:
    D[keys]=form[keys].value

password=D['Pass']
m=md5.new()                         
m.update(password)
hashedpass=str(m.hexdigest())

a=open('../data/combos.txt','r')
data=a.read()
a.close()
if D['user'] in data:
    page='Username taken. Please try a new username.<br><a href ="Register.html"> Back </a>'
else:
    page='Registered! You can login now.<br><a href ="login.html"> Login </a>'
#edited by Derek
    f=open('../data/combos.txt','a')
    f.write(D['user']+':'+hashedpass+'\n')
    f.close()
    j=open('../data/homepages.txt','a')
    j.write(D['user']+'USER\n'+D['user']+'picture\n'+D['user']+'about\n'+D['user']+',\nENDUSER\n')
    j.close()
    #writes basic stuff for their homepage
    s=open('../data/loggedin.txt', 'a')
    s.write(D['user']+',1,'+str(cgi.escape(os.environ["REMOTE_ADDR"]))+','+str(time.strftime("%Y%m%d"))+'\n')
    s.close()
print '''
<!DOCTYPE html>
<html>

<head>
   <title>
      Register
   </title>
   <link href="//d2nqa8qx64ku3x.cloudfront.net/assets/landing-new-0ec07127ff697c975eef30ccf6decd3f.css" media="screen" rel="stylesheet" type="text/css" />
   <link href="bg.css" media="screen" rel="stylesheet" type="text/css" />
</head>

<body>
<!-- EDITED by Derek -->
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

<h1 class='tagline'>'''+page+\
'''</h1>

</div></div></div></div></div></div>
</body>
<!--Made by Gary-->
</html>'''
#made by Gary
