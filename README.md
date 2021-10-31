# inside
тестовое для inside

в директории проекта запустить команды:

1 docker-compose build                                      # собрать docker

2 docker-compose run web python manage.py migrate           # применить миграции

3 docker-compose run web python manage.py createsuperuser   # создать суперюзера (для доступа в админку)

4 docker-compose up                                         # запуск сервера


  
docker-compose run web python manage.py test                # запуск тестов

