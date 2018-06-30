#q.no.1
import re
emails="zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
e=re.findall("(\w+)@([A-Z 0-9]+)\.[A-Z]{2,4}",emails,flags=re.IGNORECASE)
print(e)

#q.no.2
import re
text="betty bought a bit of butter,but the butter was so bitter,so she bought some better butter,to make the bitter butter bettter"
t=re.findall("[bB]\w+" ,text,flags=re.IGNORECASE)
print(t)

#q.no.3
import re
sentence ="A,very very; irregular_sentence"
s= re.sub("[!@#$%^&*()_ -  ; ,. ? /']"," ",sentence)
print(s)

#optional question

tweet = "good advice! RT @TheNextWeb: What i would do differently if i was learning to code today http://t.co/lbwejopxOd cc:@garybernhardt#starts"
def clean_tweet(tweet):
    tweet=re.sub('http\S+\S*','', tweet)
    tweet = re.sub('RT|cc', '', tweet)
    tweet = re.sub('#\S+', '', tweet)
    tweet = re.sub('@\S+', '', tweet)
    tweet = re.sub('[%s]' %re.escape("""!"#$%'()*+,-./;;<=>?@[\]^-{}~"""""), '', tweet)
    tweet = re.sub('\s+', '', tweet)
    return tweet
print(clean_tweet(tweet))






