from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "APIKEY*************"
# Your Auth Token from twilio.com/console
auth_token  = "AUTHTOKEN***************"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18017506482", 
    from_="13852470188",
    body="Hey I love you! Text Caleb if this works :P")

print(message.sid)
