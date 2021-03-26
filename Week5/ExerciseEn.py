"""
Required modules: requests, bs4, lxml

Introduction:
After run this program, it will create or overwite named "output-publication.txt" file on the same directory of this program.
In that file, this program will write the Subject and Featured Authors from Teacher Huang's website
"""

import requests
import bs4

# Setup what site you wanna get the data from, declar it in variable "url"
# This program will fetch data from Teacher Huang
# url = "http://210.70.80.21/~yungchen/1092-Adv-Programming/publication.html" # Teacher Zhou's website
# url = "http://dns2.asia.edu.tw/~jdwang/PaperList.htm" # Teacher Wang's
url = "http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm" # Teacher Huang's

# To use request.get() to finish HTTP Request and get response, and put this object into variable "response"
response = requests.get(url)

# Set the encoding which is to let this program to read it, except for Teacher Zhou who is using "utf-8"
# other Teachers both are using "big5" encoding
# response.encoding = 'utf8'
response.encoding = 'big5'

# Get the HTML source from "content" attribute(str type) of "response", and put this into variable rc
rc = response.content

# Use "BeautifulSoup()" form library "bs4", it will turn the HTML(str type) into an object type of HTML, be more eazier readable for python program
# The second parameter of this function is select type which is going to parse the string from the first paramter(str type)
# This example used "html.parser" to parse "rc", about another type of second parameter can find it by search from internet
soup = bs4.BeautifulSoup(rc, 'html.parser') # 使用html.parser 解析
# soup = bs4.BeautifulSoup(rc, 'lxml') # Parse with using lxml (need to pip install lxml)

# Check HTTP Status Code from response, in code, can be found in attribute "status_code" of response
# Status Codes that common to see like: 200:OK, 404:Page Not Found, 500: Server Internal Error
if response.status_code == 200: # Status Code 200 means OK

    # Open the file that use to store data from this program fetch by website
    # If this file doesn't exist, and it will auto create by run this program
    # First Parameter: file name, Second Parameter: open mode("r":read, "w": write)
    # Parameter "encoding" is setting to which encoding you want to use to open this file
    # If the file you're going to open is a different encoding to your selected, then it may be display as garbled
    # So set encoding to "utf-8" can be normally display on most encoding browser or viewer
    f = open('output-publication.txt', 'w', encoding='utf8')

    # This program is sample of fetch Teacher Huang's website, different website have differenet HTML construct
    # So in every level you use soup.find() or soup.find_all() are choose by case situation
    # In Method(function) find() and find_all() from soup(object type) has very similar arguments
    # Both are use to find the Tag name(e.g.<p></p>) by first parameter you given
    # Second parameter use to find the class name(e.g.<p class="xxx">)
    # The different between find() and find_all(), find() returns element and its inner elements by first conform to expression you've setted in parameters
    # find_all() will return all the elements and their inner elements by all the result of elements that conform to expression, and this one will be list type, not object

    # In source HTML of Teacher Huang's website, as you can see, every single data are separated by <p class="MsoNormal"> this Tag and class
    # So use soup.find_all() Method, to find all of elements whiches are conform to expressino "Tag name=p" and "class=MsoNormal""
    # Because of the find_all() returned value is list type, so it can be iterations each data by using "for" loop
    for tagP in soup.find_all('p', 'MsoNormal'):

        # Remarks: The soup object, means parsed HTML by using "BeautifulSoup()" from "bs4"
        # This type always exist one attribute called "text", it contained the element and all of the elements inside, but it doesn't include any Tag(e.g.<xxx></xxx>)

        # To remove unnecessary symbols of each data like "Escape Character"(e.g.Wrap"\n", Indent"\t")
        # In this case, use attribute "text" of soup to remove Tag, then use method of str type "replace()", to remove "\n" and "\t"
        t = tagP.text.replace('\t', '').replace('\n', '')

        # Put this data line into output file, and add a "\n" at the tail
        # This "\n" and the "\n" removed above are different things, those removen "\n" are added by bs4
        # And they might let the data which should be in the same line go to next line
        f.write(t+'\n')

    # The final of this program, close the file which is openned in earlier
    f.close()
