#!/usr/bin/python
print 'Content-type: text/html\n\n'
import cgi, cgitb, os, time
cgitb.enable()

form=cgi.FieldStorage()
D={}
for keys in form:
    D[keys]=form[keys].value
if 'user' in D:
    user = D['user']
    activeUser=D['user']
    usernamee=D['user']
    print activeUser
#~~~~~~~~~~~~~~~~~~~ALL important values~~~~~~~~~~~~~~~~~~~~~~~~~~~~
date = time.strftime("%Y%m%d")
IP = str(cgi.escape(os.environ["REMOTE_ADDR"]))

b=open('../data/homepages.txt','r')
pagedata=b.readlines()
b.close()

h=open('../data/combos.txt','r')
combodata=h.read()
h.close()
    
j = open('../data/loggedin.txt','r')
userData = j.readlines()
j.close()

k = open('../data/loggedin.txt','r')
data = k.read()
k.close()

lines=[]
x = 0
userNum = 0
date = time.strftime("%Y%m%d")
for line in data.split('\n')[:-1]:
    lines.append(line.split(','))
    if IP == line.split(',')[2] and date == line.split(',')[3]:
        userNum = x
    x+=1

j = open('../data/loggedin.txt','r')
userData = j.readlines()
j.close()
users = []
for line in userData:
    users.append(line.strip('\n').split(','))
    
for user in users:
    if cgi.escape(os.environ["REMOTE_ADDR"]) == user[2] and user[3] == date and user[1] == '1':
        activeUser = user[0]
        print activeUser
    
#~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
h=open('../data/combos.txt','r')
data=h.read()
h.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def displayhomepage():
    #opens the homepagesfile and reads each line
    userstart=pagedata.index(activeUser+'USER\n')
    picture=pagedata[userstart+1].strip('\n')
    about=pagedata[userstart+2].strip('\n')
    messages=pagedata[userstart+3].strip('\n')
    message=''
    for userandmessage in messages.strip('\n').strip(';').split(';'):
        message+='''<div class="row">
                                <div class="span2"><h4>'''+userandmessage.split(',')[0]+'''</h4></div>
                                <div class="span6">'''+userandmessage.split(',')[1]+'''</div>
                           </div><hr>'''
    reddit=''
    j = open('../data/forms.txt','r')
    c = j.readlines()
    j.close()
    for lines in c[::-1]:
        if len(lines.split(',')) > 2:
            for x in lines.split(',')[2:]:
                reddit = reddit + '<div class="row"><div class="span2"><h4>' + x.split(';')[0] + '</h4></div><div class="span6">' + x.split(';')[1] + '</div></div><hr>'
                
    return'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Home of '''+ activeUser+ '''</title>
                <meta name"description" content="Learn more about Stuyvesant High School! Everything from facts about the school, about the teachers, student reviews are all compiled in one place!">
                <link rel="stylesheet" href="bootstrap.min.css">
                <link rel="stylesheet" href="bootstrap-responsive.min.css">
                <link rel="stylesheet" href="main.css">
                <script src="http://code.jquery.com/jquery.min.js"></script>
                <script>window.jQuery || document.write('<script src="/js/jquery-1.10.0.min.js"><\/script>')</script>
                <script src="/js/bootstrap.min.js"></script>
                <link href='http://fonts.googleapis.com/css?family=Open+Sans|Finger+Paint' rel='stylesheet' type='text/css'>
            </head>
        <div class="navbar navbar-fixed-top" style="font-family:Open Sans;">
            <div class="navbar-inner">
                <div class="container">
                    <a class="brand" href="testhp.py"><i class="icon-home" style="vertical-align:0%;"></i> Hello</a>
                        <form class="navbar-search pull-left" method="POST" action="search.py">
                            <div class="input-append">
                                <input type="text" class="span6" name="search" placeholder="Search...">
                                <button type="submit" class="btn" name="submit" value="search"><i class="icon-search"></i>Go</button>
                            </div>
                        </form>
                    <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </a>
                    <div class="nav-collapse collapse">
                        <ul class="nav pull-right">
                            <li><a href="game.py">Games</a></li>
                            <li><a href="tools.py">Tools</a></li>
                            <li><a href="reddit.py">Reddit</a></li>
                            <li><a href="users.py">Users</a></li>
                            <li class="divider-vertical"></li>
                            <li><a href="logout.py"><i class="icon-user" style="vertical-align:-10%;"></i>Logout</a></li>                        </ul>
                    </div>
                </div>
            </div>
        </div>
                <div class="container"><br><br>
                    <br>
                    <div class="row">
                        <div class="span4">
                            <img src="'''+picture+'''" style="width:260px;max-height:400px">
                            <form method="get" action="picture.py">
                                <textarea style="width:100%" rows=1 name="post" placeholder="Picture url"></textarea>
                                <button class="btn btn-inverse pull-right" name="submit" value="post">Add Picture</button>
                            </form>
                            <h3>About</h3>'''+about+'''
                            <form method="get" action="about.py">
                                <textarea style="width:100%" rows=4 name="post" placeholder="Write Something About Yourself"></textarea>
                                <button class="btn btn-inverse pull-right" name="submit" value="post">Update!</button>
                            </form>
                            <h3>Website Progress</h3>
                            <h5 style="color:#33CC33"> There's always room for improvement! <small>99%</small></h5>
                            <div class="progress progress-striped active">
                                <div class="bar" style="width:99%;"></div>
                            </div>
                        </div>
                        <div class="span8">
                            <form method="get" action="message.py">
                                <textarea style="width:100%" rows=4 name="post" placeholder="Leave a message on your wall!"></textarea>
                                <button class="btn btn-inverse pull-right" name="submit" value="post">Post</button>
                            </form>
                            <div class="page-header">
                                <h3>'''+activeUser+''''s Wall</h3>
                            </div>
                            <div class="wall">
                                <div class="row">
                                    <div class="span2"><h4>Stuy</h4></div>
                                    <div class="span6">Welcome to the site!</div>
                                </div><hr>
                                '''+message+'''
                            </div>

                            <div class="page-header">
                                <h3>Lastest Comments</h3>
                            </div>
                            <div class="wall">
                                '''+reddit+'''
                            </div>
                            
                        </div>
                </div>
            </body>
        </html>
        <!-- Edited by Derek -->
        '''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#BEGIN EDIT BY DEREK
users = []
userNumber = 0
for line in data.split('\n')[:-1]:
    users.append(line.split(':'))
for x in range(len(users)-1):
    users[x][1].strip('\n')
    if users[x][0] == activeUser:
        userNumber = x
#END EDIT
        
import md5
if 'Pass' in D:
    password=D['Pass']
else:
    password= users[userNumber][1].strip('\n')
    
m=md5.new()                             
m.update(password)
hashedpass=str(m.hexdigest())

password2= users[userNumber][1].strip('\n')

d=md5.new()                             
d.update(password2)
hashedpass2=str(d.hexdigest())
#BEGIN EDIT BY DEREK
if (activeUser in data) and (hashedpass==password2 or password ==password2):
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
        lines[userNum][1] = '1'
    s=open('../data/loggedin.txt', 'w')
    for line in range(len(lines)):
        lines[line] = ','.join(lines[line])
    number = '\n'.join(lines)
    s.write(number)
    s.close()

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
        
    activeUsers = []
    inactiveUsers = []
    for user in range(len(lines)-1):
        if lines[user][1]== '1':
            activeUsers.append(lines[user][0])
        else:
            inactiveUsers.append(lines[user][0])

    #RETURNING USER - LOGGED IN  
    if activeUser in number and cgi.escape(os.environ["REMOTE_ADDR"]) == lines[userNum][2] and date == lines[userNum][3]:
        s=open('../data/loggedin.txt', 'w')
        s.write(number)
        s.close()
    elif (cgi.escape(os.environ["REMOTE_ADDR"]) != lines[userNum][2] or date != lines[userNum][3]) and D['user'] in number:
        s=open('../data/loggedin.txt', 'w')
        lines[userNum][2] = str(cgi.escape(os.environ["REMOTE_ADDR"]))
        lines[userNum][3] = date
        for line in range(len(lines)):
            lines[line] = ','.join(lines[line])
        number = '\n'.join(lines)
        s.write(number)
        s.close()
    
#END EDIT
    print displayhomepage()
    
elif cgi.escape(os.environ["REMOTE_ADDR"]) == lines[userNum][2] and date == lines[userNum][3]:
    user=lines[userNum][1]
    usernamee=user
    print displayhomepage()
else:
    print '''<!DOCTYPE html>
<html>

<head>

<h1>Incorrect Username or Password!<br>
<a href ="login.html"> Back </h1></a>
<link href="//d2nqa8qx64ku3x.cloudfront.net/assets/landing-new-0ec07127ff697c975eef30ccf6decd3f.css" media="screen" rel="stylesheet" type="text/css" />
<link href="layout.css" media="screen" rel="stylesheet" type="text/css" />
<link href="bg.css" media="screen" rel="stylesheet" type="text/css" />
</head>
<body>
</body>
<!--Made by Gary-->
</html>
'''
#made by Gary
