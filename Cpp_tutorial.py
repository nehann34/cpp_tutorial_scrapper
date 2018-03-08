from bs4 import BeautifulSoup
import urllib.request as urllib2
import os
def writeinfile(url,filename):
    s=BeautifulSoup(urllib2.urlopen(url).read())
    f=open(filename,'w')
    for sect in s.find_all('section'):
        f.write(sect.text)
    f.close()
    
url = "http://www.cplusplus.com/doc/tutorial/"
content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

main_heading = soup.title.text
if not os.path.exists(main_heading):
	os.makedirs(main_heading)
headings=[]
for h in soup.find_all('h4'):
     if not ':' in h.text:
           headings.append(h.text)
           if not os.path.exists(main_heading+"/"+h.text):
                  os.makedirs(main_heading+"/"+h.text)
print(headings)
print()
links=[]
names=[]
for ultag in soup.find_all('ul'):
    l=[]
    n=[]
    for li in ultag.find_all('a'):
        if not '/doc' in li.get('href'):
              l.append(li.get('href'))
              n.append(li.string.replace('/','-'))
    if len(l)>0:
       links.append(l)
       names.append(n)
print(links)
print()    
print(names)
print()
for p in range(len(headings)):
    for q in range(len(links[p])):
        l=url+links[p][q]
        writeinfile(l,main_heading+"/"+headings[p]+"/"+names[p][q])
