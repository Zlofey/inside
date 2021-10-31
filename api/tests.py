import json

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class MessageTestCase(APITestCase):
    def test_get_token(self):
        username = 'testuser'
        password = 'testpass'
        self.user = User.objects.create_user(username=username,
                                             password=password)
        client = APIClient()
        response = client.post('http://testserver/api/token/', {'username': username, 'password': password}, format='json')
        response_content = json.loads(response.content.decode('utf-8'))
        self.token = response_content["access"]
        assert response.status_code == 200

    def test_write_message(self, message='hello world'):
        username = 'testuser'
        password = 'testpass'
        self.user = User.objects.create_user(username=username,
                                             password=password)
        client = APIClient()
        response = client.post('http://testserver/api/token/', {'username': username, 'password': password},
                               format='json')
        response_content = json.loads(response.content.decode('utf-8'))
        self.token = response_content["access"]
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        data = {'text': message}
        response = client.post('http://testserver/api/message/', data, format='json')
        assert response.status_code == 201

    def test_get_n_messages(self, n=10):  #1<=n<=15
        username = 'testuser'
        password = 'testpass'
        self.user = User.objects.create_user(username=username,
                                             password=password)
        client = APIClient()
        response = client.post('http://testserver/api/token/', {'username': username, 'password': password},
                               format='json')
        response_content = json.loads(response.content.decode('utf-8'))
        self.token = response_content["access"]
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # write 20 messages to db
        for i in range(1, 21):
            data = {'text': 'message #{}'.format(i)}
            client.post('http://testserver/api/message/', data, format='json')

        # get latest n messages
        response = client.post('http://testserver/api/message/', {'text': 'history {}'.format(n) }, format='json')
        print('latest messages:', *json.loads(response.content.decode('utf-8')),sep='\n')
        assert response.status_code == 200

