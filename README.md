# Тестовое задание для kodland


## Описание
Простой **сайт-блог**

У сайта есть три страницы:

- Главная страница, на которой отображается 10 последних опубликованных постов от свежих к старым. У каждого поста, помимо названия и текста, отображаются иллюстрация и  дата публикации. В шапке страницы отображается самая свежая статья.
- Страница для добавления поста с формой, содержащей поле для названия поста, поле для текста поста и поле для загрузки иллюстрации к посту. Здесь пользователь может писать и публиковать свои посты.
- Страница, на которой можно прочитать полный текст статьи (чтобы перейти на нее, нужно кликнуть на кнопку "Читать" для статьи, находящейся в шапке, либо на плитку статьи - для всех остальных статей).


## Запуск (docker)

Запустить docker-compose:

```docker-compose up```

При первом запуске для функционирования проекта обязательно выполнить миграции: 

```docker-compose exec web python manage.py migrate```
