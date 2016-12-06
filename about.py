#!/usr/bin/python
print 'Content-type: text/html\n\n'
import cgi, cgitb, os, time, md5
cgitb.enable()

#~~~~~~~~~~~~~~~~~~~puts fieldstorage in dictionary D~~~~~~~~~~~~~~~~~~~~~~~~~~


form=cgi.FieldStorage()
D={}
for keys in form:
    D[keys]=form[keys].value

print '<a href="testhp.py">Back HOME</a>'

r=open('../data/loggedin.txt','r')
data=r.readlines()
r.close()

IPaddress=str(cgi.escape(os.environ["REMOTE_ADDR"]))
for lines in data:
    if str(lines.split(',')[2])==IPaddress:
        name=lines.split(',')[0]
#gets the name of the user

p=open('../data/homepages.txt','r')
pagedata=p.readlines()
p.close()

userstart=pagedata.index(name+'USER\n')
newpagedata=''
for lines in pagedata:
    if lines==pagedata[userstart+2]:
        newpagedata+=D['post']+'\n'
    else:
        newpagedata+=lines
j=open('../data/homepages.txt','w')
j.write(newpagedata)
j.close()
