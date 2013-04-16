from django.contrib import admin
from short_message.models import Message
from short_message.models import Chat

admin.site.register(Message)
admin.site.register(Chat)
