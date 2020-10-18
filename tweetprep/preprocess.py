import re
import string
from googletrans import Translator
lang_translator=Translator()
#lang_translator.translate(tweet,dest=lang).text

Dict=""":-) - basic smiley
:) - midget smiley
,-) - winking happy smiley
(-: - left hand smiley
(:-) - smiley big face
(:-( - very unhappy smiley
,-} - wry and winking smiley
8-O - Omigod
'-) - winking smiley
:-# - my lips are scaled
:-* - kiss
:-/ - skeptical smiley
:-> - sarcastic smiley
:-@ - screaming smiley
:-d - said with a smile
:-V - shouting smiley
:-X - a big wet kiss
:-\\ - undecided smiley
:-] - smiley blockhead
;-( - crying smiley
>;-> - a very lewd remark was just made
;^) - smirking smiley
%-) - smiley after staring at a screen for 15 hours straight
):-( - nordic smiley
3:] - Lucy my pet dog smiley
:-& - tongue tied
8:-) - little girl smiley
:-)8< - big girl smiley
:-O - talkaktive smiley
:-6 - smiley after eating something spicy
+:-) - priest smiley
O:-) - angel smiley
:-< - walrus smiley
:-? - smiley smokes a pipe
:-E - bucktoothed vampire
:-Q - smoking smiley
:-}X - bow tie-wearing smiley
:-[ - vampire smiley
:-a - smiley touching her tongue to her nose
:-{ - mustache
:-{} - smiley wears lipstick
:^) - smiley with a personality
<:-l - dunce smiley
:=) - orangutan smiley
>:-> - devilish smiley
>:-l - klingon smiley
@:-) - smiley wearing a turban
@:-} - smiley just back from the hairdresser
C=:-) - chef smiley
X:-) - little kid with a propeller beanie
[:-) - smiley wearing a walkman
[:] - robot smiley
{:-) - smiley wears a toupee
l^o - hepcat smiley
}:^#) - pointy nosed smiley
(:-( - the saddest smiley
:-(=) - bucktooth smiley
O-) - message from cyclops
:-3 - handlebar mustache smiley
: = - beaver smiley
:-" - whistling smiley
P-( - pirate smiley
?-( - black eye
d:-) - baseball smiley
:8) - pigish smiley
:-7 - smirking smiley
):-) - impish smiley
:/\\) - extremely bignosed smiley
8(:-) - Mickey Mouse
([( - Robocop
:-(*) - that comment made me sick
&-l - that made me cry
:-e - disappointed smiley
:( - sad-turtle smiley
:,( - crying smiley
:-( - boo hoo
:-P - Nyahhhh!
:-S - what you say makes no sense
:-[ - un-smiley blockhead
:-C - real unhappy smiley
:-r - smiley raspberry
:-t - pouting smiley
:-W - speak with forked tongue
X-( - you are brain dead
l-O - smiley is yawning
l:-O - flattop loudmouth smiley
$-) - yuppie smiley
:-! - foot in mouth
:----} - you lie like pinnochio
O-) - smiley after smoking a banana
=:-) - smiley is a punk
=:-( - real punks never smile
3:[ - pit bull smiley
8<:-) - smiley is a wizard
:#) - drunk smiley
8-# - dead smiley
B-) - smiley wears glasses
8-) - smiley with big eyes...perhaps wearing contact lenses...
H-) - cross-eyed smiley
]-I - smiley wearing sunglasses (cool...therefore no smile, only a smirk)
V^J - smiley with glasses, seen from the left side (portrait, talking)
+-( - smiley, shot between the eyes
~:-P - smiley, thinking and steaming or: having only one single hair
`' - cat's eyes in the night
L-P - totally scrambled smiley (thats why L-P Mud exists... B)
BI - a frog"""


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
    #Dict=open("emoticons.txt","r").read().split("\n")
    #print(len(Dict))
    for i in Dict.split("\n"):
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
        try:
            if len(re.findall(r"%s"%(i[0]),tweet))>0 and flag==0:
                tweet=re.sub(r"%s"%(i[0]),"%s"%(i[1]),tweet)
                flag=1
        except:
            pass
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
