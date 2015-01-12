#!/usr/bin/python
#coding=utf-8

import urllib2
import xml.etree.cElementTree as ET
import datetime
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

import	sys
reload(sys)
sys.setdefaultencoding('utf8')

# do something
def writeFile(fileName, string):
	#f = open('./'+ datetime.datetime.now().strftime("%H%M%S %B-%d-%Y-") + fileName, 'w')
	f = open('./htm/'+ datetime.datetime.now().strftime("%H%M%S %B-%d-%Y ") + fileName, 'w')
	#f = open('./'+ datetime.datetime.now().strftime("%H%M%S-") + fileName, 'w')
	f.write(string)
	f.close()
##	end


##	Redirect
def URLRedirect():
	#req = urllib2.Request('http://r.search.yahoo.com/_ylt=A2oKmLvDk1xTMicAztyzygt.;_ylu=X3oDMTFkcjVsYm9lBHNlYwNvdi10b3AEY29sbwNzZzNfaW50bAR2dGlkA1ZJUEhLNTNfMQRwb3MDMw--/RV=2/RE=1398604868/RO=10/RU=http%3a%2f%2f2970009.r.msn.com%2f%3fld%3dDvnHbBe2PpNBcp1oQAlOMQVTVUCUx4umsDHTnvace_0BfEe7QTTvrbYttW-qq7Sd_a4_MvBeTeIqvb4IWiyjPomHpDFCfwx5B0Mn5FwTT8cBm8nfY0tZ3gJ1ot4R09nEMl20PA9Q2Zvc98dyZTZKMKKE2hQfE%26u%3dwww.glhkg.com%252f/RK=0/RS=gaW1s0jbsQN3uOjPpoFj9Ibnr_E-?p=%E8%A3%9C%E7%BF%92')
	#req = urllib2.Request('http://money18.on.cc/info/liveinfo_quote.html?symbol=01829')
	req = urllib2.Request('http://www.aastocks.com/tc/ltp/rtquote.aspx?symbol=01777')
	res = urllib2.urlopen(req)
	finalurl = res.geturl()

	response = urllib2.urlopen(finalurl)
	html = response.read()
	writeFile("money18.htm", html)
	response.close()  # best practice to close the file

	soup = BeautifulSoup(''.join(html))       # 讀進BeautifulSoup
	#soup = BeautifulSoup(html.decode(cp950))       # 讀進BeautifulSoup
	#print "[SOAP]:", soup
	print "title:", soup.title
	#print "Ftitle:", soup.find_all('a')
	#print "Ftitle:", soup.find(class="cf4.6")
	#for article in soup.findAll("div", {'class':'tb-h2'}):
    #print "Title: " + article.a.contents[0]
    #print "Link: " + article.a['href']
    #print ""
	#print html

	#req = urllib2.Request(starturl, datagen, headers)
	#res = urllib2.urlopen(req)
	#finalurl = res.geturl()

## end


##	URL call
def URLRequest():

	#response = urllib2.urlopen('http://r.search.yahoo.com/_ylt=A2oKmJjmeldTVQkAYyKzygt.;_ylu=X3oDMTFjNWswNnRjBHNlYwNvdi10b3AEY29sbwNzZzNfaW50bAR2dGlkA0hLQzAwOF8xBHBvcwMz/RV=2/RE=1398270822/RO=10/RU=http%3a%2f%2f2690298.r.msn.com%2f%3fld%3dDviDbEWHBf7tDmsfa0lg3o1zVUCUyduBQSJGi64P2hCMvrs4LaXQ34j0K9j8HpI2vlzDJb_z9gIaFNAncXO6rST5yjOS0nMW9xjUg-uCnM-1Q6dCXXFGxQdxenDlvKWwmQUOSlGp8J5MQN5FCJO3xqRoRd3Ms%26u%3dwww.tutorok.com/RK=0/RS=FMeCztUSWidvL3.QJU5PYu8WDpM-?p=%E9%A6%99%E6%B8%AF%E8%A3%9C%E7%BF%92')
	#req = urllib2.Request('http://r.search.yahoo.com/_ylt=A2oKmJjmeldTVQkAYyKzygt.;_ylu=X3oDMTFjNWswNnRjBHNlYwNvdi10b3AEY29sbwNzZzNfaW50bAR2dGlkA0hLQzAwOF8xBHBvcwMz/RV=2/RE=1398270822/RO=10/RU=http%3a%2f%2f2690298.r.msn.com%2f%3fld%3dDviDbEWHBf7tDmsfa0lg3o1zVUCUyduBQSJGi64P2hCMvrs4LaXQ34j0K9j8HpI2vlzDJb_z9gIaFNAncXO6rST5yjOS0nMW9xjUg-uCnM-1Q6dCXXFGxQdxenDlvKWwmQUOSlGp8J5MQN5FCJO3xqRoRd3Ms%26u%3dwww.tutorok.com/RK=0/RS=FMeCztUSWidvL3.QJU5PYu8WDpM-?p=%E9%A6%99%E6%B8%AF%E8%A3%9C%E7%BF%92')

	respYahooList = urllib2.urlopen('https://hk.search.yahoo.com/search?p=%E8%A3%9C%E7%BF%92&fr=yfp-s&ei=UTF-8&meta=rst%3Dhk')
	htmlYahooList = respYahooList.read();
	return htmlYahooList
## end



##	Search Result Page
def keywordSearch():
	keyword = u'補習'
	keyword = keyword.encode('utf-8')
	url = "https://hk.search.yahoo.com/search?p=" + keyword + "&fr=yfp&ei=UTF-8&meta=rst%3Dhk"
	respYahooList = urllib2.urlopen(url)
	htmlYahooList = respYahooList.read();
	#writeFile("yahoo.htm", htmlYahooList)

	return htmlYahooList
## end



def doMyHTMLParser(htmlYahooList):
	# instantiate the parser and fed it some HTML
	parser = MyHTMLParser()
	parser.feed(htmlYahooList)
	#parser.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')


def mini(xml_string):
	import xml.dom.minidom

	#xml = xml.dom.minidom.parse(xml_fname) # or
	xml.dom.minidom.parseString(xml_string)
	pretty_xml_as_string = xml.toprettyxml()


from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data



htmlYahooList = keywordSearch()
#htmlYahooList = URLRequest()

#print htmlYahooList

#root = ET.fromstring(htmlYahooList)
#string_data = open('file.xml')
#string_data = open(htmlYahooList)

#x = ET.fromstring(htmlYahooList)
#root = ET.fromstring(file.xml)


'''
tree = ET.parse(htmlYahooList)

root = tree.getroot()


#root = ET.fromstring(htmlYahooList)


for country in root.findall('country'):
	#print child.tag, child.attrib
	name = country.get('name')
	print "DO: ",name, rank
'''

#doMyHTMLParser(htmlYahooList)
#mini(htmlYahooList)

URLRedirect()

##	Print info
'''
print response.info()
print html
'''

#import sys
#print sys.getdefaultencoding()

