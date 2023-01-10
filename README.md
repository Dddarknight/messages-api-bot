# messages-api-bot

The application provides the opportunity to receive user's messages, pushed to API, in telegram bot.
Main steps:
1. You need to register in the API app.
2. You receive your jwt-token in the API app. Then you have to use it in headers of requests.
3. You push your token to the API app. Also you push the same token to the bot to make a connection between API and the bot.
4. You send the message to the API app. After that you receive this message from the bot in the form "{Your-name}, I received a message from you. \n {your-message}".


| Endpoint | Method | Description |
|----------|---------|---------|
| /docs | GET |  API documentation with Swagger/OpenAPI 2.0 specifications. |
| /api/users/sign-up/ | POST |  Creates a user. |
| /api/users/token/ | GET |  Returns a jwt-token for the API app. To use the token in /docs you need to add 'Bearer your-token' after clicking Authorize button. |
| /api/messages/tg-token/ | POST |  Creates a token for the bot. |
| /api/messages/tg-token/ | PUT |  This endpoint is used in the bot to connect the chat in the bot and the API user. |
| /api/messages/ | POST |  Creates user's message. |
| /api/messages/ | GET |  Returns the list of authenticated user's messages, including their content and the date of creation. |


<a href="https://codeclimate.com/github/Dddarknight/messages-api-bot/test_coverage"><img src="https://api.codeclimate.com/v1/badges/0f9e7c3cac3e182c38bb/test_coverage" /></a>

## Links
This project was built using these tools:
| Tool | Description |
|----------|---------|
| [Django ](https://www.djangoproject.com/) |  "A high-level Python web framework" |
| [Django REST framework](https://www.django-rest-framework.org/) |  "A powerful and flexible toolkit for building Web APIs" |
| [Python Telegram Bot](https://docs.python-telegram-bot.org/en/stable/index.html#) | "This library provides a pure Python, asynchronous interface for the Telegram Bot API" |
| [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html) |  "Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API." |
| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |

### App on Heroku (API and Bot):
[![Heroku-API](https://pyheroku-badge.herokuapp.com/?app=shielded-thicket-58235)](https://shielded-thicket-58235.herokuapp.com/docs/)

[![Heroku-Bot](https://pyheroku-badge.herokuapp.com/?app=messages-bot)](https://messages-bot.herokuapp.com/)

[Bot](https://t.me/messages_factory_bot)


## Installation

**Copy a project**
```
$ git clone git@github.com:Dddarknight/messages-api-bot.git
$ cd messages-api-bot
```

**Set up environment variables**
``` 
$ touch .env

# You have to fill .env file. See .env.example.
# You will have to:
# 1) You have to write into .env file SECRET_KEY for Django app.
# To get SECRET_KEY for Django app:
$ python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
# 2) TG_API_TOKEN is your telegram bot token, given after its creation.
# 3) HEROKU_APP and TG_APP are filled with the names of API and Bot applications after the deployment on Heroku.
```

**Set up the environment**
```
$ pip install poetry
$ make install
```

**Launch API server**
```
$ make run
```

**Launch Bot**
```
$ make bot_
```

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)