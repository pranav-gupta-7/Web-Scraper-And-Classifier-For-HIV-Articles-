import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import spacy
nlp = spacy.load('en_core_web_lg')

data=pd.read_excel('final.xlsx')

count=data['Class'].value_counts()
_class=count.index.values
count=list(count)

#death articles visualization
years=data.loc[data['Class']==7]
year_count=years['Year'].value_counts()
year_count=year_count.sort_index()
year_val=year_count.index.values
year_count=list(year_count)

plt.figure()
plt.plot(year_val,year_count)
plt.xlabel('Years', fontsize=18)
plt.ylabel('No. of death articles ', fontsize=18)
plt.show()

#suicide articles visualization
years=data.loc[data['Class']==8]
year_count=years['Year'].value_counts()
year_count=year_count.sort_index()
year_val=year_count.index.values
year_count=list(year_count)

plt.figure()
plt.plot(year_val,year_count)
plt.xlabel('Years', fontsize=18)
plt.ylabel('No. of suicide articles ', fontsize=18)
plt.show()


#bargraph for number of articles from each category
plt.figure(figsize=(10,9))
plt.bar(_class,count,linewidth=.8)
plt.xticks(_class,_class)
plt.xlabel('Class/Category', fontsize=18)
plt.ylabel('No. of articles ', fontsize=18)
plt.show()

#marriage articles visualization
doc=data.loc[data['Class']==4]
articles=doc.iloc[:,3]
marriage_string = ""
word = "wedding marriage matrimonial "
r = Rake(language='english')
r.extract_keywords_from_text(word)
tags = r.get_ranked_phrases()
for tag in tags:
    tokens = set(word_tokenize(tag))
    for token in tokens:
        curr_tag = stemmer.stem(token)
        if curr_tag not in marriage_string:
            marriage_string += curr_tag + " "

#classifing marriage reports articles
n=0
marriage_article_no=[]
for article in articles:
    r = Rake(language='english')
    r.extract_keywords_from_text(article)
    tags = r.get_ranked_phrases()
    for tag in tags:
            tokens = set(word_tokenize(tag))
            for token in tokens:
                curr_tag = stemmer.stem(token)
                if curr_tag  in marriage_string:
                  marriage_article_no.append(n)
                  
    n=n+1 
marriage_articles_year=[]
for a in marriage_article_no:
    marriage_articles_year.append(doc.iloc[a,0])

years= pd.DataFrame(marriage_articles_year,columns=['Year']) 
year_count=years['Year'].value_counts()
year_count=year_count.sort_index()
year_val=year_count.index.values
year_count=list(year_count)

plt.figure(figsize=(6,6))
plt.bar(year_val,year_count)
plt.xlabel('Years', fontsize=18)
plt.ylabel('No. of Marriage/Matrimony articles ', fontsize=14)
plt.xticks(year_val,year_val)
plt.show()


# finding places mentioned in the surge areas category

headings=data.loc[data['Class']==5]
headings=headings.iloc[:,3]
place=[]
label=[]
for heading in headings:
  doc = nlp(heading) 
  for ent in doc.ents:
    place.append(ent.text)
    label.append(ent.label_)
a=0
places=[]
while a<len(label):
  if label[a]=='GPE' or label[a]=='ORG':
    places.append(place[a])
  a=a+1 
places=list(set(places))

#pie cahrt
count=data['Class'].value_counts()
count=count.sort_index()
count=list(count)   
total_sum=sum(count) 
avg=np.divide(count,total_sum)
percentage=np.multiply(avg,100)

label=[0,1,2,3,4,5,6,7,8]
plt.figure(figsize=(7,7))
plt.pie(percentage,labels=label, autopct="%1.1f%%")
plt.axis('equal')

plt.show()
