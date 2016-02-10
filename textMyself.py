#textMyself.py - Defines the testmyself() function that texts a message
#passed to it as a string

#preset values
accountSID = 'ACe82dbe7ffab30be824aa90960cd6effe'
authToken = 'a6d0f9335c4a4bee972d2b2a01b7a347'
myNumber = '+13366154419'
twilioNumber = '+13368142293'

from twilio.rest import TwilioRestClient

def textmyself(message):
	twilioCli = TwilioRestClient(accountSID,authToken)
	twilioCli.messages.create(body=message,from_=twilioNumber,to=myNumber)
	
