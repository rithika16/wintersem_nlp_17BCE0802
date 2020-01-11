#!/usr/bin/env python
# coding: utf-8

# In[2]:


from nltk.corpus import stopwords
stopwords.words('english')


# In[3]:


from nltk.corpus import stopwords
stopwords.words('French')


# In[4]:


from nltk.corpus import stopwords
stopwords.words('german')


# In[5]:


import nltk 
entries = nltk.corpus.cmudict.entries()
len(entries)


# In[6]:


for entry in entries [10000:10025]:
    print(entry)


# In[7]:


from nltk.corpus import wordnet as wn
wn.synsets("phone") # you get an id for subsets.
wn.synsets("house")


# In[8]:


wn.synset('call.v.03').lemma_names()


# In[9]:


wn.synset('telephone.n.01').lemma_names()


# In[10]:


wn.synset('family.n.01').lemma_names()


# In[11]:


texts = [""" Christopher Hemsworth born 11 August 1983 is an Australian actor. He rose to prominence playing Kim Hyde in the Australian TV series Home and Away (2004–07) 
before beginning a film career in Hollywood by taking on parts in the science fiction film Star Trek (2009) and the thriller A Perfect Getaway (2009).
Hemsworth went on to star in the fantasy film Snow White and the Huntsman (2012), the war film Red Dawn (2012), the action thriller Blackhat (2015), 
the biographical thriller In the Heart of the Sea (2015),
the comedy Ghostbusters (2016), and the Men in Black film series spin-off Men in Black: International (2019). 
His most critically acclaimed roles include the comedy horror The Cabin in the Woods (2012) and the biographical sports film Rush (2013), in which he portrayed James Hunt.
"""]

#the text from wikipedia about chris hemsworth.
for text in texts:
    sentences =nltk.sent_tokenize(text)
    for sentence in sentences:
        words =nltk.word_tokenize(sentence)
        tagged_words =nltk.pos_tag(words)
        print(tagged_words)


# In[12]:


import nltk
from nltk.tokenize import TweetTokenizer
text =' After years of rebuilding OTHER nations, we are finally rebuilding OUR nation. We are finally putting AMERICA FIRST! :) ' #Donald J trump Tweet
twtkn =TweetTokenizer()
twtkn.tokenize(text)


# In[13]:


from nltk.corpus import brown
news_text =brown.words(categories ='news')
fdist =nltk.FreqDist(w.lower() for w in news_text)
modals =['can','could','may','might','must','will','what']
for m in modals:
    print(m+ ':',fdist[m],end='\n ')


# In[ ]:




