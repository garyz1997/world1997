#!/usr/bin/python
print 'Content-type: text/html\n\n'
import cgi, cgitb, os, time, random
cgitb.enable()
#page made by Derek

NumList = [] ## list of numbers to guess ##
while len(NumList)<5:
    y = random.randint(1,20)
    if y not in NumList:
        NumList.append(y)
NumList.sort()
print NumList

form=cgi.FieldStorage()
D={}
for keys in form:
    D[keys]=form[keys].value

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

j=open('../data/loggedin.txt', 'r')
number=j.read()
j.close()
lines=[]
x = 0
userNum = 0
date = time.strftime("%Y%m%d")
for line in number.split('\n'):
    lines.append(line.split(','))

activeUsers = []
inactiveUsers = []
for user in range(len(lines)-1):
    if lines[user][1]== '1':
        activeUsers.append(lines[user][0])
    else:
        inactiveUsers.append(lines[user][0])

#BEGIN GAMES DATA
k=open('../data/games.txt', 'r')
games = k.read()
k.close()

gameUsers = games.split('\n')

gameUsersList = []  #list of users playing games
userID = -1
x=0
for user in gameUsers:
    gameUsersList.append(user.split(';')[0])
    if activeUser == user.split(';')[0]:
        userID = x
    x+=1

numScores = []      #list of scores for Guess the Number

for user in gameUsers:
    numScores.append(user.split(';')[1])

NumList2 = []
matches = 0
if 'num1' in D and 'num2' in D and 'num3' in D and 'num4' in D and 'num5' in D:
    NumList2.append(D['num1'])
    NumList2.append(D['num2'])
    NumList2.append(D['num3'])
    NumList2.append(D['num4'])
    NumList2.append(D['num5'])
    NumList2.sort()
    for x in range(5):
        if int(NumList2[x]) in NumList:
            matches += 1
    list = numScores[userID].split(',')
    list.append(str(matches))
    numScores[userID] = ','.join(list)

out =''
for x in range(len(gameUsersList)):
    out += gameUsersList[x] + ';' + numScores[x] + ';\n'
out = out.strip('\n')

tot = 0
x=0  
l=open('../data/games.txt', 'w')
l.write(out)
l.close()

for score in numScores[userID].split(','):
    tot += float(score)
    x+=1.0
avgNum = tot / x

def Error():
    print'''
<!DOCTYPE html>
<html>

<head>
   <title>
      Guess the number
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

listSelect = ''
for x in range(20):
    listSelect += '<option value="' + str(x+1) +'">' + str(x+1) + '</option>'
    
if activeUser == '':
    Error()
else:
    print'''
<!DOCTYPE html>
<html>

<head>
   <title>
      GAMES Page
   </title>
</head>
<body bgcolor="#D9CCB9">
<div style="position:relative;width:84%;height:100%;float:left;padding:5px;">

<div style = "font-size:8">Welcome<b>
'''+str(activeUser)+'''</b>!</div>
<div style = "font-size:8;text-align:right;"><a href="logout.py">Logout</a>!</div>

<center><table border="0">
<tr>
<td colspan="3" style="background-color:#D9CCB9;padding:5px;">
<h1><center><img src=../data/games.png></center></h1>
</td>
</tr>
<tr>
<td style="background-color:#EEEEEE;width:300px;padding:5px;">
<b>Info</b><br>
Username: <b>'''+str(activeUser)+''' </b><br>
Time: <b>'''+str(datetime)+'''</b><br> 
Posts: BEEP
</td>
<td style="background-color:#EEEEEE;height:200px;width:500px;padding:5px;">

    <b> Guess five different numbers between 1 and 20!</b><br>
<form action = "num.py" method = "post">
<select name="num1">'''+listSelect+'''</select><select name="num2">'''+listSelect+'''</select><select name="num3">'''+listSelect+'''</select><select name="num4">'''+listSelect+'''</select><select name="num5">'''+listSelect+'''</select>
<input type = 'submit' value = 'Guess!'>
</form>

</td></tr>
<tr>
<td style="background-color:#EEEEEE;width:300px;padding:5px;">
<b>Average Number of Matches:</b> '''+str(avgNum)+'''<br>
</td>
<td style="background-color:#EEEEEE;height:200px;width:500px;padding:5px;">

</td> </tr> </table></center>
</div>

<div style="position:relative;width:14%;height:100%;float:right;background-color:#EEEEEE;padding:5px;">
Your IP: '''+str(cgi.escape(os.environ["REMOTE_ADDR"]))+'''<p>Active Users:<br>
'''
    for user in activeUsers:
        print str(user) + "<br>"

    print '''
</p><p>Inactive Users:<br>
'''
    for user in inactiveUsers:
        print str(user) + "<br>"
    print '''
</p>
</div>
<!--Made by Derek-->
</body>
</html>'''

    
#page made by Derek
