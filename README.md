# Web-Scraper-And-Classifier-For-HIV-Articles

<h2>Categories used for classification-</h2>
1- Support/Facilitation/Awareness<br>
2- Research/Development/Biomedical Improvement<br>
3- Society Discrimination/Negative Impact<br>
4- Patient’s progress/Infected improved life<br>
5- Surge/HIV positive cases<br>
6- HIV negative cases<br>
7- Accident/Death cases<br>
8- Suicide Cases<br>
0- other<br><br>
  
<h2>Requirrements-</h2>
1-Python<br>
2-NLTK<br>
3-Keras<br>
4-Matplotlib (for visualization)<br>
5-Spacy (for extracting places names from the articles)

<h2>How to use the repo</h2>
1. Firstly run news_articles_url_scrapper.py. It will scrap all the articles from a given date to another and will dump all the urls in a CSV file named all_articles.csv<br>
2. Then run hiv_article_dataset_creator.py. It will scrap all the HIV articles from the all_articles.csv fille and a create hiv_report_data.xlsx file containing columns Year,Heading and Content of the HIV article.<br>
3. Running the Classifier.ipynb will classifiy the HIV articles on the above given categories.<br>
4. Run visualization.py if you want to get the visualized report on (death cases,suicide cases,matrimony related articles and the places mentioned in surge/epidimic  category).
