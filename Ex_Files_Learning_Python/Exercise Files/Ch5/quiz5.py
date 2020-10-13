import urllib.request
import json


# Question 1 of 8
# Can you print all cities and states in this JSON data, and what approach will you take if you can?
data = [ { "country": [
        { "city": "New York", "state": "NY" },
        { "city": "Boston", "state": "MA" }
  ]},
  { "country": [
        { "city": "Quebec", "state": "QC" },
        { "city": "Toronto", "state": "ON" }
  ]} ]

for i in data:
    for j in i["country"]:
        print(j)
# answer:It is possible, by using one for i in theJSON loop and within it another nested for j in i["country"] loop.

# Question 2 of 8
# The following code, which is supposed to dump the google.com homepage HTML to the console, is missing a line at the ??? placeholder. What should this line be?
import urllib.request
webUrl = urllib.request.urlopen("http://www.google.com")
results = webUrl.read()
print(results)

# Question 3 of 8
# Given the XML below, how will you add a third item to the list that has a yellow color and a small size?
# <?xml version="1.0" encoding="UTF-8" ?>
# <catalog>
#   <item color="blue" size="large"/>
#   <item color="red" size="medium"/>
# </catalog>
# # answer:
# doc = xml.dom.minidom.parse("my.xml")
# newItem = doc.createElement("item")
# newItem.setAttribute("color", "yellow")
# newItem.setAttribute("size", "small")
# doc.firstChild.appendChild(newItem)

# Question 4 of 8
# Given the following JSON data stored in a theJSON object, how can you list only the skill names?
# theJason = {
#     "name": "John",
#     "title": "Python Developer",
#     "skills": [{
#         "name": "coding",
#         "level": "expert"
#         },
#         {
#         "name": "documentation",
#         "level": "basic"
#     }]
# }
# for i in theJason["skills"]:
#     print(i["name"])

# Question 5 of 8
# What value should be returned by the URL request getcode() call to confirm that the specified site can be properly connected to?
# answer: 200

# Question 6 of 8
# What class does Python provide to parse HTML?
# HTMLParser

# Question 7 of 8
# The statement below fails when you try to run it. Which troubleshooting step is irrelevant for this scenario
# doc = xml.dom.minidom.parse("myfile")
# confirm:
# in the local folder
# is a valid xml file
# already import xml.dom.minidom
# do not need to Confirm that the file 'myfile' is first loaded to memory.

# Question 8 of 8
# For the HTML file below, how many times will the handle_starttag() and handle_endtag() methods of the Python-provided HTML parser class be called?
<div class="sidebar">
  <img src="pic.gif" height="50" width="100" />
  <button type="button" id="btn-submit">Submit</button>
</div>
# You are correct!
# 3 and 3