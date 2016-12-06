#!/usr/bin/python
print 'Content-type: text/html\n\n'
import cgi, cgitb, os, time
cgitb.enable()
#page made by Derek

form = cgi.FieldStorage()
j = open('../data/loggedin.txt','r')
userData = j.readlines()
j.close()
users = []
for line in userData:
    users.append(line.strip('\n').split(','))

#check user sequence
activeUser = ''
date = time.strftime("%Y%m%d")
datetime = time.strftime("%m/%d %H:%M")
for user in users:
    if cgi.escape(os.environ["REMOTE_ADDR"]) == user[2] and user[3] == date and user[1] == '1':
        activeUser = user[0]


def Error():
    print'''
<!DOCTYPE html>
<html>

<head>
   <title>
      GAMES Page
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

<h1 class='tagline'>
You are no longer logged in!
</h1>
<h3 class='tagline'>
Your session may have timed out or you are on a different computer.
</h3>
<br>
Try to <a href='index.html'>login</a> again.
<br>
'''+cgi.escape(os.environ["REMOTE_ADDR"])+'''
</div></div></div></div></div></div></div></div>
<!--Made by Derek-->
</body>
</html>
'''
    
def Forum(): #start a thread!
    j = open('../data/forms.txt', 'r')
    f = j.readlines()
    j.close()
    forums = ''
    r = ''
    b = ''
    if len(f) > 0:
        for lines in f:
            r = lines.split(',')[0]
            b = lines.split(',')[1]
            forums = forums + '<tr> <td style="background-color:#EEEEEE;">' + r + '</td> <td style="background-color:#EEEEEE;">' + b + '</td> </tr>'
    page ='''<html>
<head>
        <meta charset="utf-8">
        <title>Reddit</title>
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
<body>
<br><br><br>
<div class="container">
'''
    form = cgi.FieldStorage()
    page += '''<center><table border="0" width = "100%">
<tr>
<td style="background-color:#EEEEEE;">
<b>Info</b><br>
Username: ''' + str(activeUser) + ''' <br>
</td>
<td style="background-color:#EEEEEE;height:200px;">
<form action="reddit.py" method="get">
    <font size="6"> <b> Start a Thread! </b><br> </font> <input type="text" name="thread" style="height:75px; width:50%; font-size:35px;"><br>
    <input type="hidden" name="action" value="disc">
    <input type="submit" value="submit"></form></td>
</tr>
<tr>
<td style="background-color:#EEEEEE;"> <b>Username</b> </td>
<td style="background-color:#EEEEEE;"> <b>Threads</b> </td></tr>''' + forums + '''
    </table></center>'''
    page += '</div></body> </html>'
    print page
def disc(): #add new thread
    p = open('../data/forms.txt','a')
    p.write(str(activeUser) + ',<a href="reddit.py?action=comment&thread=' + form['thread'].value + '">' + form['thread'].value + '</a>\n')
    p.close()
def comment(): #show thread contents
    j = open('../data/forms.txt','r')
    c = j.readlines()
    j.close()
    form = cgi.FieldStorage()
    charles = ''
    y = '<a href="reddit.py?action=comment&thread=' + form['thread'].value + '">' + form['thread'].value + '</a>'
    for lines in c:
        if lines.split(',')[1].strip('\n') == y:
            if len(lines.split(',')) > 2:
                for x in lines.split(',')[2:]:
                    charles = charles + '<tr> <td style="background-color:#EEEEEE;width:150px;">' + x.split(';')[0] + '</td> <td style="background-color:#EEEEEE;width:150px;">' + x.split(';')[1] + '</td> </tr>'
    page ='''<html>
        <head>
        <meta charset="utf-8">
        <title>GAMES</title>
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
                        <form class="navbar-search pull-left" method="POST" action="/search.py">
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
        <div class="container">
<body>
<br><br><br>
'''
    form = cgi.FieldStorage()
    page += '''<center><table border="0" width = 100%>
<tr>
</tr>
<tr>
<td style="background-color:#EEEEEE;" width = '20%'>
<b>Info</b><br>
Username: ''' + str(activeUser) + ''' <br>
</td>
<td style="background-color:#EEEEEE;height:200px;">
    <font size="12"> <b><a href="reddit.py?action=comment&thread=''' + form['thread'].value + '''">''' + form['thread'].value + '''</a></b></font><br>
</tr>
<input type="hidden" name="action" value="disc">
<tr>
<td style="background-color:#EEEEEE;"> <b>Username</b> </td>
<td style="background-color:#EEEEEE;">
<b>Comments</b>
</td> </tr>''' + charles + '''
<tr style="background-color:#EEEEEE;">
<td>''' + str(activeUser) + '''</td>
<td>
<br>
<form action="reddit.py" method="get">
<input type="text" name="text" style="height:25px;"><input type="hidden" name="action" value="commenting"><input type="hidden" name="thread" value="''' + form['thread'].value + '''">
<input type="submit" value="submit"></form>
</td>
</tr>
    </table></center>'''
    page += '</body></div> </html>'
    print page
def commenting(): #comment in thread
    p = open('../data/forms.txt','r')
    j = p.readlines()
    p.close()
    form = cgi.FieldStorage()
    f = ''
    x = '<a href="reddit.py?action=comment&thread=' + form['thread'].value + '">' + form['thread'].value + '</a>'
    for lines in j:
        if lines.split(',')[1].strip('\n') == x:
            f = f + lines.strip('\n') + ',' + '<a href="profile.py?username=' + str(activeUser) + '">' + str(activeUser) +  '</a>' + ';' + form['text'].value + '\n'
        else:
            f = f + lines
    p = open('../data/forms.txt', 'w')
    p.write(f)
    p.close()
    
if activeUser == '':
    Error()
elif 'action' in form.keys():
    if form['action'].value == 'disc':
        disc()
        Forum()
    elif form['action'].value == 'comment':
        comment()
    elif form['action'].value == 'commenting':
        commenting()
        comment()
    else:
        Forum()
else:
    Forum()

