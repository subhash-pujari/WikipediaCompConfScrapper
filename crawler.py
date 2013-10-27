import re
import sys
import urllib2
from bs4 import BeautifulSoup



#html parser
def htmlParser(content):
	soup = BeautifulSoup(content)


	h2_headings = list()
	h2_list = soup.find_all('h2')
	
	for i in h2_list:
		soup = BeautifulSoup(i.__str__())
		tag = soup.span
		#print type(tag)
		if tag:
			h2_headings.append(tag['id'])
			print tag['id']
		else:
			h2_headings.append('no id')
			print 'no id'
		
		#print i

	print len(h2_list)

	#get the index for <h2>
	startIndex = [a.start() for a in list(re.finditer('<h2>', content))]

	#get the index for </h2>	
	endIndex = [a.end() for a in list(re.finditer('</h2>', content))]
	
	#initialise the list		
	domainStringList = list()

	#get the string between 2 headings
	for i in range(len(startIndex)-1):
		domainStringList.append(content[endIndex[i]:startIndex[i+1]])
	

	for str in domainStringList:
		soup = BeautifulSoup(str)
		li = soup.find_all('li')
		for i in li:
			if i:
				string = i.a.contents
				if string[0].find('/') == -1:
					print string[0]
	print len(domainStringList)


#http client
def httpClient(url):
	request = urllib2.Request( url , headers={'User-Agent' : "Magic Browser"})
	f = urllib2.urlopen(request)
	return f.read()		


def main():
	args = sys.argv
	url = args[1]
	content  = httpClient(url)
	htmlParser(content)

#the main function declaration
if __name__ == "__main__":
	main()
