from selenium import webdriver
import time
# Using Chrome to access web
driver = webdriver.Chrome(r"C:\Users\visha\chromedriver")

# Open the website/url
driver.get('https://www.youtube.com/watch?v=G73C-kC1IfM')
driver.execute_script('window.scrollTo(1, 500);')

#now wait let load the comments
time.sleep(3)
for i in range(0,25000,500):
    b = 'window.scrollTo('+ str(0) +','+ str(0+1000) +');'
    driver.execute_script(b)
    time.sleep(2)
    i = i+500
    
comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
j = []
for comment in comments:
    v = comment.text
    j.append(v)
driver.close()

newlist = []
for k in range(0,len(j)):
    edf = j[k].split()
    newlist.append(edf)

jk = []
for i in range(0,len(newlist)):
    k = newlist[i]
    jk = jk+k

l = [i.lower() for i in jk]  # it has to be lower case so that STOP words can be eliminated later by STOPWORD package 

#from nltk.probability import FreqDist
#fdist1 = FreqDist(l) #with stop words
#fdist1.plot(10)

############################################################

'removing STOP words'
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english')) #some words are just plain useless, and are filler words

SW = []
for k in l:
    if k not in stop_words:
        SW.append(k)
from nltk.probability import FreqDist
fdist = FreqDist(SW)
fdist.plot(5,cumulative=True) #this will plot the frquency plot for 5 most occuring words in commnets
