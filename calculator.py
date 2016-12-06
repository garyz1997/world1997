#!/usr/bin/python
import cgi, cgitb, math
cgitb.enable()
print 'Content-type: text/html\n\n'

form=cgi.FieldStorage()

def fact(number):
    ans=number
    for num in range(number)[1:]:
        ans*=num
    return ans

def main():
    end=''
    command=''
    error=0
    if 'the_commands' in form:
        commands=form['the_commands'].value
        if 'start' not in commands:
            start=1
            command="WHERE'S YOUR START FUNCTION???"
            error=1
        if 'print' not in commands:
            command+="WHERE'S YOUR PRINT FUNCTION???"
            error=1
        for lines in commands.split('\r\n'):
            lines=lines.strip(' ')
            command+='<br>'+lines
            if 'start' in lines:
                try:
                    start=float(lines[6:])
                except:
                    command+=' <-- NOT A NUMBER'
                    start=0
                    error=1
            elif 'add ' in lines:
                try:
                    start+=float(lines[4:])
                except:
                    command+=' <-- NOT A NUMBER'
                    error=1
            elif 'sub ' in lines:
                try:
                    start-=float(lines[4:])
                except:
                    command+=' <-- NOT A NUMBER'
                    error=1
            elif 'div' in lines:
                try:
                    if float(lines[4:])==0:
                        command+=' <-- DIVIDE BY 0 ERROR'
                        error=1
                    else:
                        try:
                            start=float(start)/float(lines[4:])
                        except:
                            command+=' <-- NOT A NUMBER'
                            error=1
                except:
                    command+=' <-- NOT A NUMBER'
                    error=1
            elif 'expt' in lines:
                try:
                    start=start**int(lines[5:])
                except:
                    command+=' <-- NOT A NUMBER'
                    error=1
            elif 'mult' in lines:
                try:
                    start*=float(lines[5:])
                except:
                    command+=' <-- NOT A NUMBER'
                    error=1
            elif '!' in lines:
                try:
                    start=fact(int(start))
                except:
                    command+=' <-- NOT A NUMBER'
                    error=1
            elif 'sqrt' in lines:
                try:
                    start=math.sqrt(int(start))
                except:
                    command+=' <-- NOT A NUMBER'
                    error=1
            elif 'abs' in lines:
                if start >=0:
                    try:
                        start=start
                    except:
                        command+=' <-- NOT A NUMBER'
                        error=1
                else:
                    try:
                        start=0-start
                    except:
                        command+=' <-- NOT A NUMBER'
                        error=1
            elif 'print' in lines:
                end=start
            else:
                command+=' <-- FUNCTION NOT FOUND'
                error=1
        if error==0:
            command=command.strip('<br>')
            page='<html><body background="http://www.colourbox.com/preview/4325026-16953-vector-colorful-fireworks-on-white-background.jpg">'
            page+='''<h2 align="center">Your Commands:</h2> <font size="3" color="#4B0082"><center>'''+str(command)+'</center></font>'
            page+='''<h2 align="center">The Answer:</h2> <font size="3" color="#006400"><center>'''+str(end)+'</font>'
            page+='''<br><br><img src="http://cdn.arkarthick.com/wp-content/uploads/2011/11/entrepreneur-leadership-skills-good-job-whos-awesome.jpg">'''
            page+='''<form method="GET" action="calculator.html"><input type="submit" name="Calc" value="Back to Calculator"></form></center>'''
            page+='</body></html>'
            print page
        else:
            newcom=str(command)
            newcom=newcom.replace('<br>','\n')
            newcom=newcom.strip('\n')
            page='''<html>
          <head>
            <meta http-equiv="content-type" content="text/html; charset=windows-1252">
              <title>Calculator</title>
          </head>
          <body background="http://www.collegetocareers.com/wp-content/uploads/2010/09/cd-rates-calculator.bmp" link="#006400" vlink="#A52A2A">
            <h2 align="center">Calculator</h2>
            <center>
            <p><a href="Instructions.html">Here are the instructions.</a></p>
            <table border="1" width="35%" cellpadding="7" cellspacing="0">
              <tr>
                <td width="30%">
                <form method="POST" action="calculator.py">
                  <table border="1" width="100%" cellspacing="0" cellpadding="5" bgcolor="#B0E0E6">
                    <tr>
                      <td width="100%">
                        <p align="center"><font color="#FF0000" size="4"><b>Commands</b></font></p></td>
                    </tr>
                    <tr>
                      <td width="100%">
                        <p align="center">
        <textarea rows="20" name="the_commands" cols="30">'''+newcom+'''</textarea></p>
                      </td>
                    </tr>
                    <tr>
                      <td width="100%">
                        <p align="center"><input type="submit" value="Calculate!" name="Calc"></p>
                      </td>
                    </tr>
                  </table>
                </form>
            </table>
        </center>
        </body>
        </html>'''
            print page
    else:
        command='WHERE ARE YOUR FUNCTIONS??'
        newcom=str(command)
        newcom=newcom.replace('<br>','\n')
        newcom=newcom.strip('\n')
        page='''<html>
          <head>
            <meta http-equiv="content-type" content="text/html; charset=windows-1252">
              <title>Calculator</title>
          </head>
          <body background="http://www.collegetocareers.com/wp-content/uploads/2010/09/cd-rates-calculator.bmp" link="#006400" vlink="#A52A2A">
            <h2 align="center">Calculator</h2>
            <center>
            <p><a href="Instructions.html">Here are the instructions.</a></p>
            <table border="1" width="35%" cellpadding="7" cellspacing="0">
              <tr>
                <td width="30%">
                <form method="POST" action="calculator.py">
                  <table border="1" width="100%" cellspacing="0" cellpadding="5" bgcolor="#B0E0E6">
                    <tr>
                      <td width="100%">
                        <p align="center"><font color="#FF0000" size="4"><b>Commands</b></font></p></td>
                    </tr>
                    <tr>
                      <td width="100%">
                        <p align="center">
        <textarea rows="20" name="the_commands" cols="30">'''+newcom+'''</textarea></p>
                      </td>
                    </tr>
                    <tr>
                      <td width="100%">
                        <p align="center"><input type="submit" value="Calculate!" name="Calc"></p>
                      </td>
                    </tr>
                  </table>
                </form>
            </table>
        </center>
        </body>
        </html>'''
        print page
main()
