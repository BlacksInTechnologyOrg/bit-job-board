import json
import logging
from flask_app.utils import hashid
from flask_app.models.messaging import Conversation, Message
from mongoengine.queryset.visitor import Q


class MessageHandler:
    def newMessage(self, username, recipient, subject, content):
        try:
            conversation = Conversation()
            usermessage = Message()
            id = hashid()

            # Conversation Collection
            conversation.conversationId = id
            conversation.participants = [username, recipient]
            conversation.save()

            # Message Collectioin
            usermessage.author = username
            usermessage.recipient = recipient
            usermessage.subject = subject
            usermessage.content = content
            usermessage.conversationId = id
            usermessage.save()
        except Exception as e:
            logging.error(e)

    def getAllMessages(self, username, pagenumber):
        pgnumber = int(pagenumber)
        items_per_page = 5
        offset = (pgnumber - 1) * items_per_page
        try:
            messages = (
                Message.objects(
                    Q(author__exact=username) | Q(recipient__exact=username)
                )
                .order_by("conversationId", "modified_at")
                .skip(offset)
                .limit(items_per_page)
                .to_json()
            )
            return messages
        except:
            logging.error(Exception)

    def deleteMessage(self, messageid):
        message = Message.objects(id__exact=messageid)
        if not message:
            raise TypeError("Message ID not found")
        else:
            message.delete()
