import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room, Message
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Called when the websocket connection is opened.
        We use the room_name in the URL (e.g. /ws/chat/5/) to build the group name.
        """
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        # Fetch room from DB (safe)
        self.room = await Room.objects.aget(name=self.room_name)

        # Use the room.id as the group name (safe for Channels)
        self.room_group_name = f"chat_{self.room.id}"
        # Join the websocket group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """
        Called when websocket is closed.
        Remove this channel from the group.
        """
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Called whenever a message is received from the websocket.
        We save the message to the database and broadcast it to the group.
        """
        data = json.loads(text_data)
        message_content = data['message']

        user = self.scope['user']
        room = await database_sync_to_async(Room.objects.get)(name=self.room_name)
        # Save the message
        await database_sync_to_async(Message.objects.create)(
            room=room,
            sender=user,
            content=message_content
        )
        # Broadcast the new message to all users in the same group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender': user.username,
                'message': message_content,
            }
        )

    async def chat_message(self, event):
        """
        Called by the channel layer to send the message to the client.
        """
        await self.send(text_data=json.dumps({
            'sender': event['sender'],
            'message': event['message'],
        }))