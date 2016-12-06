#!/usr/bin/python
print 'Content-type: text/html\n\n'
import cgi, cgitb, os, time, md5
cgitb.enable()

form=cgi.FieldStorage()
D={}
for keys in form:
    D[keys]=form[keys].value

if 'countryshow' in D:
    page='''<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=windows-1252">
      <title>'''+'Countries in '+str(D['continent'])+'!'+'''</title>
    <style> 
body
{
background:url("http://www.psdgraphics.com/file/glowing-world-map-background-1280x960.jpg");
background-size:1700px 900px;
padding-top:40px;
}
</style>
  </head><font color="chartreuse">'''+\
  'Countries in '+str(D['continent'])+'!'
    e=open('countries.txt','r')
    data=e.read()
    e.close()
    if D['continent'] in data:
        continentplace=data.split('\n').index(D['continent']+':')
    for lines in data.split('\n')[:continentplace+1:-1]:
        if ':' in lines:
            endpoint=data.split('\n').index(lines)
    countries=data.split('\n')[continentplace+1:endpoint]
    page+='<table border=1>'
    for country in countries:
        page+='<tr><td><font color="chartreuse">'+str(country)+'</td></tr>'
    page+='</table>'
    print page
if 'continentshow' in D:
    page='''<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=windows-1252">
      <title>'''+'Countries in '+str(D['country'])+' is in:<br>'+'''</title>
    <style> 
body
{
background:url("http://www.psdgraphics.com/file/glowing-world-map-background-1280x960.jpg");
background-size:1700px 900px;
padding-top:40px;
}
</style>
  </head><font color="chartreuse">'''+\
  str(D['country'])+' is in:<br>'
    e=open('countries.txt','r')
    data=e.read()
    e.close()
    countryplace=data.split('\n').index(D['country'])
    for lines in data.split('\n')[:countryplace+1]:
        if ':' in lines:
            continent=lines.strip(':')
    page+=continent
    print page
