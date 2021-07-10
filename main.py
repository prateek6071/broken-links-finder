from selenium import webdriver
from time import sleep
import pandas as pd
from webdrivermanager.chrome import ChromeDriverManager
import requests as requests
import sys

print(sys.argv[1])

driver = webdriver.Chrome(executable_path= sys.argv[1])
driver.get('https://www.thrilleasy.com/index.html')


def findalllinks(url):
    driver.get(url)
    links = driver.find_elements_by_tag_name("a")
    links= list(set(links))
    for link in links:
        if 'https://www.thrilleasy.com' not in str(link.get_attribute('href')):
            p=link.get_attribute('href')

            brokenlinkdata.append(p)


        else:
            linkname = link.get_attribute('href')
            if (requests.head(linkname).status_code == 200):

                if ((str(link.get_attribute('href')) not in (processedlinks or duplicatelinks) and str(link.get_attribute('href')) != 'https://www.thrilleasy.com/coming-soon.html') and ('thrilleasy' in str(link.get_attribute('href')) and str(link.get_attribute('href')) not in ['https://www.thrilleasy.com/post.html', 'https://www.thrilleasy.com/post.html','https://www.thrilleasy.com/index.html#'])):

                    linkdata.append(str(link.get_attribute('href')))
                    processedlinks.append(str(link.get_attribute('href')))
                    duplicatelinks.append(str(link.get_attribute('href')) + '#')
                    linkname = link.get_attribute('href')
                    #if (linkname not in ['https://www.thrilleasy.com/Contact.html#', 'https://www.thrilleasy.com/Contact.html']):

                    print(brokenlinkdata)
                    findalllinks(str(linkname))



            else:
                    brokenlinkdata.append(link.get_attribute('href'))






linkdata=[]
brokenlinkdata=[]
processedlinks=[]
duplicatelinks=[]
findalllinks('https://www.thrilleasy.com/index.html')

print(brokenlinkdata)
