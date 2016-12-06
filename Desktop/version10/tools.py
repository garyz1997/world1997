#!/usr/bin/python
print 'Content-type: text/html\n\n'
import cgi, cgitb, os, time
cgitb.enable()
#page made by Derek

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

    
if activeUser == '':
    Error()
else:
    print'''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>TOOLS</title>
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
        <div class="container">
                    <h1>Admin2 <small><span class="pull-right"><button class="btn btn-info" onclick="location.href='edit.py'">Settings</button></small></h1>
                    <br>
        </div>
<body>
<center>
<table><tr>
<td>
<ul class="middle">
    <li><a href="calculator.html"><center>Calculator<br><img src=https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRxQXsuLp6RzsoQDewDQYJboTASc0W3nJioGclbg2enVa-YFZCmEw></a></li>
    <li><a href="countryfinder.html"><center>Country Finder<br><img src=http://a.dryicons.com/images/icon_sets/shine_icon_set/png/256x256/world.png></a></li>
</ul>
</td>
</tr></table></h1>
</body>
<!--Made by Gary-->
</html>'''
