import json
from flask_application.utils import hashid
from flask_application.users.models import Conversation, Message

def newMessage(current_user,recipient,subject,content):
    conversation = Conversation()
    usermessage = Message()

    # Conversation Collection
    conversation.conversationId = hashid()
    conversation.participants = [current_user.username, recipient]
    conversation.save()

    # Message Collectioin
    usermessage.author = current_user.username
    usermessage.recipient = recipient
    usermessage.subject = subject
    usermessage.content = content
    usermessage.conversationId = Conversation.objects(
        participants__exact=[current_user.username, recipient]).first().conversationId
    usermessage.save()

    return "success"

def getMessages(username):
    messages = []
    allconvosids = [convoquery.conversationId for convoquery in Conversation.objects(
        participants__contains=username)]
    for convoid in allconvosids:
        messagequery = Message.objects(conversationId__exact=convoid).to_json()
        messagequery = json.loads(messagequery)
        for message in messagequery:
            messages.append(message)

    return messages
