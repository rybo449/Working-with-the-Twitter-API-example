import tweepy, io
import time
import json
import sets
from sets import Set

# Consumer keys and access tokens, used for OAuth
consumer_key =  "cpiu5ihMVP61vV7u29X9Q"
consumer_secret = "yZRASVjToEwdgi3bDfc5Wav2vDiIXdVZbcDPZ51LI"
access_token = "2199546091-jWBzm6vNqBk1tRyOfh6ABGEWBeqvzm5DJjEozR7"
access_token_secret = "o3hEOOIqNtTGJdIFSfvYYlX9K8oIF2a9vQVI6T92Cy3JA"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

f = open("xaj","r")
lines = f.readlines()
f.close()

f1 = open("donexaj","r")
lines1 = f1.readlines()
f1.close()

s1 = Set(lines)
s2 = Set(lines1)

s1 = s1.difference(s2)

lines = list(s1)

for line in lines:    
    ids_fers=[]
    ids_fing=[]
    line = line.strip('\n')

    try:
        for page in tweepy.Cursor(api.followers_ids, line, count=5000).pages():
            ids_fers.extend(page)
            time.sleep(60)
            
        for page in tweepy.Cursor(api.friends_ids, line, count=5000).pages():
            ids_fing.extend(page)
            time.sleep(60)
                
        print line
        obj = { "user" : line, "followers" : ids_fers, "following" : ids_fing}
                
        w = open(line, "w")
        w.write(json.dumps(obj, indent = 4))
        w.close()

    except tweepy.TweepError as e:
        e1 = open("error","a+")
        e1.write(line + "\t" + str(e.message) + "\t"+ str(e.args) +'\n')
        e1.close()
     
    done = open("done" + "xaj","a+")
    done.write(line + '\n')
    done.close()
