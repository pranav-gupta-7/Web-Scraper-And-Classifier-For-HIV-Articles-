import pandas as pd
from bs4 import BeautifulSoup
import requests


data=pd.read_csv("all_articles.csv")
archive=data.iloc[:,:].values

#dataset creation
hiv_dataset=pd.DataFrame(columns=['Date','Headline','Content'])


hiv_articles_url=[]
defect=[]
def hiv_articles_finder(archive):
 words_list=['-HIV-','/HIV-','/HIV/','-HIV/','-AIDS-','/AIDS-','/AIDS/','-AIDS/']
 a=0
 hiv_urls=[]
 while a<archive.size:
    url=archive[a,0]
    if any(word in url for word in words_list):
        hiv_urls.append(url)
    a=a+1    
 return hiv_urls   

def hiv_article_dataset_creation(hiv_articles_url,hiv_dataset):
    size=len(hiv_articles_url)
    a=0
    defect=[]
    while a<size:
        url=hiv_articles_url[a]
        try:
         page=requests.get(url)
         soup=BeautifulSoup(page.content,'html5lib')
        
         heading=soup.find('arttitle').get_text()
         content=soup.find('div',class_='Normal').get_text()
         time=soup.find_all('time')
         time=str(time)
         time=time[17:27]
        
         hiv_dataset=hiv_dataset.append(pd.Series([time,heading,content], index=hiv_dataset.columns ), ignore_index=True)
        except Exception:
            print("not "+str(a))
            defect.append(a)
        
        print(str(a)+" completed")
        a=a+1
        
        
    return hiv_dataset,defect
   
     
hiv_articles_url=hiv_articles_finder(archive)  
hiv_dataset,defect=hiv_article_dataset_creation(hiv_articles_url,hiv_dataset)

#sorting articles according to date
hiv_dataset=hiv_dataset.sort_values('Date')
  
#saving to local machine       
writer = pd.ExcelWriter('hiv_report_data.xlsx')
hiv_dataset.to_excel(writer,'Sheet1')       
writer.save()
