#First import the required libraries
import twitter, datetime
import urllib2
import sqlite3

console = sqlite3.connect("C:\Users\andre\AppData\Local\Google\Chrome\User Data\Default\History")
cursor = console.cursor()

cursor.execute("SELECT urls.title FROM urls")
rows = cursor.fetchall()

recent = []

for row in rows:
    recent.append(row)
    
lastTitle = str(recent[-1])
title = lastTitle[3:-3]
print(title)
console.close

#Hardcore a user ID into a variable
##user =  791988154693742592

#Load in my keys and secrets from the credentials file into a list (array)
file = open("keys.txt")
creds = file.read().split('\n')

#Create a new API wrapper, passing in my credentials one at a time
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

#Get the most recent batch of status updates from the user
##statuses = api.GetUserTimeline(user)

#Find out what time it is now (in Coordinated Universal Time)
timestamp = datetime.datetime.utcnow()

#Post status update and get the response from Twitter
##response = api.PostUpdate("Tweeted at " + str(timestamp))
response = api.PostUpdate("My last viewed page was: " + title)
#Just print out the most recent one
##print (statuses [0].text)
##print("Status updated to: " + response.text)

print("My last viewed page was: " + title)