#!/bin/bash
PROJECTS_DIR=/code
STATIC_DIR=$PROJECTS_DIR/static

set -e



echo "== Установка зависимостей =="

python -m pip freeze > requirements.txt



echo "== Инициализация git-репозитория =="
git init
cp $STATIC_DIR/.gitignore .

git config --global user.email "artbyter@gmail.com"
git config --global user.name "Art"

echo "== Первый коммит =="
git add .
git commit -m "Старт проекта"

echo "== Создание приложения webapp =="
python manage.py startapp webapp
mv templates webapp/templates
mkdir webapp/static
mkdir webapp/static/css webapp/static/js
sed --in-place="" "s/\(.*\)'django.contrib.staticfiles',/\1'django.contrib.staticfiles',\n\1'webapp',/g" home44/settings.py

echo "== Второй коммит =="
git add .
git commit -m "Создание приложения webapp"

echo "== Подключение Bootstrap =="
cp $STATIC_DIR/jquery.min.js webapp/static/js
cp $STATIC_DIR/popper.min.js webapp/static/js
cp $STATIC_DIR/bootstrap/css/bootstrap.css webapp/static/css
cp $STATIC_DIR/bootstrap/js/bootstrap.min.js webapp/static/js

echo "== Третий коммит =="
git add .
git commit -m "Подключение Bootstrap 4"

echo "== Инциализация проектных скриптов и стилей =="
touch webapp/static/js/main.js
touch webapp/static/css/style.css

echo "== Четвёртый коммит =="
git add .
git commit -m "Инициализация стилей и скриптов проекта"

echo "== Создание базового шаблона =="
cp $STATIC_DIR/base.html webapp/templates

echo "== Пятый коммит =="
git add .
git commit -m "Создание базового шаблона"

echo "== Создание базы данных sqlite3 =="
python manage.py migrate

echo "== Создание суперадмина =="
python manage.py createsuperuser

echo "== Настройка проекта завершена. Для дальнейшей работы настройте проект в вашем любимом редакторе или IDE или запустите сервер. =="
