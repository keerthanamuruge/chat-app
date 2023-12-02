import json
from channels.generic.websocket import WebsocketConsumer
from user.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        

    def disconnect(self, close_code):
        pass
    def receive(self, data):
        data_json = json.loads(data)
        reciever_data = data_json.get('reciever')
        receiver = User.objects.get(id = reciever_data.get("id"))

        message = reciever_data.get('message')
        self.send(text_data=json.dumps({
            'message': message
        }))