from bs4 import BeautifulSoup 
import urllib.request
import csv
import requests
import re


year=2010 #Starting year
month=1   #Starting month
day=1     #starting day
checks=40179


months_list1=[1,3,5,7,8,10]
months_list2=[4,6,9,11]
months_list3=[2]

leap_year=[2012,2016]
article_links=[]
n=0

while checks < 40543:
   
    url="https://timesofindia.indiatimes.com/"+str(year)+"/"+str(month)+"/"+str(day)+"/archivelist/year-"+str(year)+",month-"+str(month)+",starttime-"+str(checks)+".cms"
    
    page=requests.get(url)
    #page=urllib.request.urlopen(url)
    soup=BeautifulSoup(page.content,'html5lib')
    all_links=soup.find_all('a')
    for link in all_links:
        match = re.search(r'http://timesofindia.indiatimes.com//.*\.cms', str(link))
        if match:
           article_links.append(match.group(0))
    
    if month==12 and day==31:
       month=1
       day=1
       year=year+1
       print("year "+ str(year)+" completed\n")
       
       
    elif month in months_list1 and day==31:
        print("month-"+ str(month) +"\n")
        month=month+1
        day=1
   
        
    elif month in months_list2 and day==30:
        print("month-"+str(month)+"\n")
        month=month+1
        day=1
       
        
    elif month in months_list3 and year in leap_year and day==29:
        print("month-"+str(month)+"\n")
        month=month+1
        day=1
       
         
    elif month in months_list3 and year not in leap_year and day==28:
        print("month-"+str(month)+"\n")
        month=month+1
        day=1   
        
         
    else:
        day=day+1
                     
    n=n+1    
    checks=checks+1    
 
# Saving to local machine     
with open('new'+str(year)+'.csv','w') as file:
         csv_output=csv.writer(file,quoting=csv.QUOTE_ALL,delimiter='\n')
         csv_output.writerow(article_links)    

