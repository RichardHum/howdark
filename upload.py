#!/usr/bin/python

import os
import commands
import cgi, cgitb
import cv2
import numpy

cgitb.enable()
print "Content-type: text/html"
print 
print "<html>"
print "<head>"
print "<title>How dark are my skies?</title>"
print "</head>"
print "<body>"
print 'Your skyfog is: '
form = cgi.FieldStorage()
filedata = form['upload'].value

image = cv2.imdecode(numpy.frombuffer(filedata,dtype=numpy.uint8),0)

imgFlat = image.ravel()

med = numpy.median(imgFlat)

pct = med/255 * 100

exp = float(form['exp'].value)
iso = float(form['iso'].value)
ap = float(form['ap'].value)

mag = 13.93+2.5*numpy.log10(exp * (iso / 800)*(50 / pct)*(4 / ap)*(4 / ap))

print round(mag,3)

print "mag/arc sec^2"

if mag < 17.8:
   bortle = 9
elif mag < 18.38:
    bortle = 8
elif mag < 18.95:
    bortle = 7
elif mag < 19.5:
    bortle = 6
elif mag < 20.49:
    bortle = 5
elif mag < 21.25:
    bortle = 4.5
elif mag < 21.69:
    bortle = 4
elif mag < 21.89:
    bortle = 3
elif mag < 21.99:
    bortle = 2
elif mag < 22:
    bortle = 1
else:
    bortle = "That's an impossible sky brightness! Double check your inputs!"

print "<br>"
print "Your Bortle magnitude is approximately "
print bortle

print "<br><a href=\"/\">Go back</a>"
print "<br>"
print "<br>"
print 'Sky brightness to bortle conversion was taken from this table by Attilla Danko: <a href="http://www.cleardarksky.com/lp/ChrSprPkPAlp.html">http://www.cleardarksky.com/lp/ChrSprPkPAlp.html</a>'
print "</body>"
print "</html>"
