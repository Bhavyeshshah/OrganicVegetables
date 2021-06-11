from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
        .create(
    body='Thankx for registration',
    from_ ='+14847200081',
    to_ ='+918898892174',

    )

print(message.sid)