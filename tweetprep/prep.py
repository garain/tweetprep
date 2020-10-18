import re
import string
from googletrans import Translator
lang_translator=Translator()
#lang_translator.translate(tweet,dest=lang).text


def remove_USER(tweet):
    template=r"@[a-zA-Z0-9]+"
    tweet1=re.sub(template,'',tweet)
    return tweet1    
    
def remove_hashtags(tweet):
    template = r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)" 
    tweet1 = re.sub(template, '', tweet)
    return tweet1

def remove_mentions(tweet):
    template = r'(?:@[\w_]+)'
    tweet1 = re.sub(template, '', tweet)
    return tweet1

def remove_punctuation(tweet):
    translation = str.maketrans('', '', string.punctuation)
    return tweet.translate(translation)

def remove_urls(tweet):
    template = r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'
    tweet1 = re.sub(template, '', tweet)
    return tweet1

def contract_whitespace(tweet):
    tweet = tweet.replace('\n', ' ')
    tweet1 = re.sub("\s\s+", " ", tweet.strip())
    return tweet1

def replace_emoji(tweet):
    Emoji_dict=[]
    Dict=open("emoticons.txt","r").read().split("\n")
    #print(len(Dict))
    for i in Dict:
        Emoji_dict.append(i.split(" - "))
    #try:
    emo_final=[]
    for i in Emoji_dict:
        j=i[0]
        try:
            j=re.sub(r"\(","\\(",j)
        except:
            pass
        try:
            j=re.sub(r"\)","\\)",j)
        except:
            pass
        try:
            j=re.sub(r"\]","\\]",j)
        except:
            pass
        try:
            j=re.sub(r"\[","\\[",j)
        except:
            pass            
        try:
            j=re.sub(r"\^","\\^",j)
        except:
            pass
        try:            
            j=re.sub(r"\*","\\*",j)
        except:
            pass   
        try:
            j=re.sub(r"\$","\\$",j)
        except:
            pass  
        try:
            j=re.sub(r"\.","\\.",j)
        except:
            pass 
        try:
            j=re.sub(r"\+","\\+",j)
        except:
            pass
        try:
            j=re.sub(r"\?","\\?",j)
        except:
            pass
        emo_final.append([j,i[1]])
    flag=0
    for i in emo_final:
        if len(re.findall(r"%s"%(i[0]),tweet))>0 and flag==0:
            tweet=re.sub(r"%s"%(i[0]),"%s"%(i[1]),tweet)
            flag=1
        
    return tweet
#    except:
#        return tweet


def partitioner(hashtag,words):
    while hashtag:
        word_found=longest_word(hashtag,words)
        yield word_found
        hashtag=hashtag[len(word_found):]
        
def longest_word(phrase,words):
    current_try=phrase
    while current_try:
        if current_try in words or current_try.lower() in words:
            return current_try
        current_try=current_try[:-1]
    return phrase

def split_uppercase(s):
    r = []
    l = False
    for c in s:
        # l being: last character was not uppercase
        if l and c.isupper():
            r.append(' ')
        l = not c.isupper()
        r.append(c)
    return ''.join(r)

def partition_hashtag(text, words):
    return re.sub(r'#(\w+)',lambda m:''.join(partitioner(m.group(1),words)),text)
                  
def read_dictionary_file(tweet):
    return set(word.strip() for word in tweet)

def clean(tweet):
    tweet1 = replace_emoji(tweet)    
    tweet2=remove_USER(tweet1)
    #tweet = remove_hashtags(tweet)
    tweet3 = partition_hashtag(tweet2,read_dictionary_file(tweet2))
    tweet4 = split_uppercase(tweet3)
    tweet5 = remove_mentions(tweet4)
    tweet6 = remove_urls(tweet5)
    tweet7 = remove_punctuation(tweet6)
    tweet8 = contract_whitespace(tweet7)
    #tweet0 = lang_translator.translate(tweet1,dest="es").text
    return tweet8.lower()

'''
tweets = ["The UN calls on #TrumpAdministration to stop separating immigrant children from parents #UnitedNations... https://t.co/SFGZ8MLcvk https://t.co/hhOwoAhPpi"]
for t in tweets:
    print(t)
    print(clean(t))
'''
