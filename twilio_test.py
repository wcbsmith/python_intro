from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6e4f1458c8a96d2c65b0ae9e4e0462a5"
# Your Auth Token from twilio.com/console
auth_token  = "abe05dcdfa87ecbf005cdd2fd0b58aee"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18017506482", 
    from_="13852470188",
    body="Hey I love you! Text Caleb if this works :P")

print(message.sid)
