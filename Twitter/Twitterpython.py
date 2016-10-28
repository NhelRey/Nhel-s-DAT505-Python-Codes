import twitter, datetime

#user = 	362774577

file = open("res/TwitterCredentials.txt")
creds = file.read().split('\n')

api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

timestamp = datetime.datetime.utcnow()

response = api.PostUpdate("Tweeted at " + str(timestamp))

print("Status updated to: " + response.text)