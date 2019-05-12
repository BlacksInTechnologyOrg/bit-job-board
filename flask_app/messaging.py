import json
import logging
import uuid
from .models.messaging import Conversation, Message
from mongoengine.queryset.visitor import Q
from .errors import MessageNotFoundError


class MessageHandler:
    def newMessage(self, username, recipient, subject, content):
        try:
            conversation = Conversation()
            usermessage = Message()
            id = uuid.uuid1().hex

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
        except Exception:
            logging.error(Exception)

    def deleteMessage(self, messageid):
        message = Message.objects(id__exact=messageid)
        if not message:
            raise MessageNotFoundError
        else:
            message.delete()
