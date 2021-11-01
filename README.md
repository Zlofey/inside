# inside
тестовое для inside

в директории проекта запустить команды:
```
# собрать docker (порт 5432 должен быть свободен)
docker-compose build		

# применить миграции
docker-compose run web python manage.py migrate		

# создать суперюзера (для доступа в админку)
docker-compose run web python manage.py createsuperuser     

# запуск сервера
docker-compose up                                                 	


# запуск тестов
docker-compose run web python manage.py test                        
```

можно затестить онлайн:


[heroku](https://inside-test.herokuapp.com/)

[админка](https://inside-test.herokuapp.com/admin) (test_user, test_pass)

примеры запросов:

```
запрос токена
	curl  -X POST  \
	-H "Content-Type: application/json"  -d '{"username": "test_user", "password": "test_pass"}' \
	https://inside-test.herokuapp.com/api/token/

написать сообщение
  curl -X POST \
  -H "Authorization: Bearer <полученный Token>" \
  -H "Content-Type: application/json"  -d '{"text": "<Ваш текст>"}' \
  https://inside-test.herokuapp.com/api/message/

получить 1<=n<=15 своих последних сообщений
  curl -X POST \
  -H "Authorization: Bearer <полученный Token>" \
  -H "Content-Type: application/json"  -d '{"text": "history <число от 1 до 15>"}' \
  https://inside-test.herokuapp.com/api/message/

```
