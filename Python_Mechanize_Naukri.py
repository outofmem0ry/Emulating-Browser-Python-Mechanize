#!/usr/bin/python -tt
#Create a browser object and give it some optional settings.
import mechanize
import random
br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

#Open a webpage 
#Open a webpage and inspect its contents

response = br.open('http://www.naukri.com/')
# print response.read()      # the text of the page
response1 = br.response()  # get the response again
# print response1.read()     # can apply lxml.html.fromstring()
# Using forms
# List the forms that are in the page
# for form in br.forms():
    # print "Form name:", form.name
    # print form
# To go on the mechanize browser object must have a form selected
# br.select_form("form1")       works when form has a name
br.form = list(br.forms())[2]  # use when form is unnamed

# User credentials
br.form['USERNAME'] = raw_input("Enter username")
br.form['PASSWORD'] = raw_input("Enter Password")

# for control in br.form.controls:
   # if control.type == "submit":
       # control.disabled = True

# Submit the form
# When your form is complete you can submit

response = br.submit()
# print response.read()
br.back()   # go back
# Finding Links
# Following links in mechanize is a hassle because you need the have the link
# object.

# Sometimes it is easier to get them all and find the link you want from the text.
# links = open('link.txt','w') File created to see all the links

for link in br.links():
  if link.text == 'IT Skills':
    request = br.click_link(link)
    response = br.follow_link(link)
    urltoupdate = br.open(response.geturl())
    for form in br.forms():
        #print "Form name:", form.name
        br.form = br.form = list(br.forms())[0]
        for control in br.form.controls:
            #print control.type,control.name, control.value
            if control.type =='select' and control.name == 'expYear[]':
                if control.value != ['-1']:
                    #value = [['06'],['07'],['08']]
                    control.value = ['3']
        response = br.submit()
        #print response.read()