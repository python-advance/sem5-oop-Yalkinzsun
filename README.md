#### Инвариантная самостоятельная работа

2.1 Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).

Был создан родительский класс Post, в котором определён метод `__init__()`. Необязательный аргумент title, равный None, нужен, а точнее не нужен для дочерних классов, так как у комментария к записи нет заголовка. Также в этом классе импортируются 2 библиотеки: **uuid** и **datetime**. Они нужны для генерации уникального значения и взятия текущей даты и времени сооствественно. В методе `__init__()` хранится список всех комментариев: `self.comments = list()` 

```Python
class Post:
   def __init__(self, author, content, title=None):
        import uuid
        import datetime
        self.author = author
        if title is not None:
            self.title = title
        self._content = content
        self.id = uuid.uuid4()
        self.date = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
        self.comments = list()
```
Метод `show()` выводит на экран информацию о записи
```Python
    def show(self):
        print("Date: " + str(self.date))
        print("Id: " + str(self.id))
        print("Author: " + str(self.author))
        print("Content: " + str(self._content))
```
Метод `show_comments()` выводит на экран информацию о всех комментариях к записиэ
```Python
    def show_comments(self):
        for comment in self.comments:
            comment.show()
            print()
```
От класса `Post` был относледован класс `Comment`. Функция `super` (также можно было написать `super().__init__()`) позволяет использовать метод `__init__()` родительского класса
```Python
class Comment(Post):
    def __init__(self, author, content):
        #используем метод __init__ суперкласса
        super(Comment, self).__init__(author=author, content=content)
```
2.2. Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга». Создание функций для вывода на печать информации, хранящийся в объектах.

Добавление геттеров и сеттеров для контента
```Python
@property
    def content(self):
        return self._content

    def add_comment(self, comment):
        self.comments.append(comment)
    
    @content.setter
    def content(self, content):
        self._content = content
    
    @content.getter
    def content(self):
        return self._content
```
#### Вариативная самостоятельная работа

3.1 Разработка прототипа приложения “Регистрация на конференцию” на основе фрагмента технического задания с использованием ООП.

Был создан родительский класс `Event`, в котором определён метод `__init__`. Используются библиотеки **uuid** и **re** для генерации уникального значения и для использования регулярных выражений соотвественно. Есть проверка введённой даты, при неверном формате которой, поднимается исключение. 

```Python
class Event:
    def __init__(self, name, date, description):
        import uuid
        import re
        self.name = name
        date_re = re.compile(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}")
        if (not(date_re.findall(str(date)))):
           raise ValueError('Invalid date! Right format is "day/month/year"')
        else:
           self.date = date
        self.description = description
        self.id = uuid.uuid4().hex
```
Определяем сеттеры и гетторы
```Python
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @name.getter
    def name(self):
        return self._name
```
Создан новый класс `ITConference`, унаследованный от родительского класса `Event` . Данный класс содержит список `members` , для хранения данных об учтастниках. Метод `__init__()` полностью наследуются от родительского. Метод  `add_member` позволяет добавить нового участника. Метод `show` выводит информацию на экран об участнике. Метод `show_members` выводит информацию о всех участниках
```Python
class ITConference(Event):
    members = []
    def __init__(self, name, date, description):
        Event.__init__(self, name, date, description)

    def add_member(self, member):
        self.members.append(member)
    
    def show(self):
        print("Date: " + str(self.date))
        print("Id: " + str(self.id))
        print("Name: " + str(self.name))
        print("Description: " + str(self.description))
    
    def show_members(self):
        for member in self.members:
            member.show()
            print()
```
Также создан класс `Member` c несколькими проверками с ипользованием регулярных выражений в определённом методе `__init__()`
```Python
class Member:
    def __init__(self, nickname, name, surname, email, birthday):
        import re
        self.nickname = nickname
        self.name = name
        self.surname = surname
        email_re = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if (not(email_re.findall(str(email)))):
           raise ValueError('Invalid email!"')
        else:
           self.email = email
        birthday_re = re.compile(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}")
        if (not(birthday_re.findall(str(birthday)))):
           raise ValueError('Invalid birthday! Right format is "day/month/year"')
        else:
           self.birthday = birthday
```
`Show()` - ещё один метод для класса `Member`, выводящий на экран информацию иб участнике
```python
    def show(self):
        print("Nickname: " + str(self.nickname))
        print("Name: " + str(self.name))
        print("Surname: " + str(self.surname))
        print("Email: " + str(self.email))
        print("Birthday: " + str(self.birthday))
```
3.4 Разработка скрипта для получения и сохранения данных социальных сетей Twitter, Instagram или VK.

Для реализации скрипта были использованы следующие библиотеки:

- vk -  для работы с API Вконтакте 
- json - для работы с JSON-структурами
- re - для создания регклярных выражений
- datetime - для форматированного вывода текущего времени

Также необходимо наличие ключа доступа (token), который можно получить на [этой](https://vkhost.github.io) странице. Или просто пароль и логин от личного аккаунта. 

Небольшая проверка для токена на наличие допустимых символов:

```Python
pattern = r'[^\.a-z0-9]'
  token = "YOUR TOKEN"
  if re.search(pattern, token):
    print('Invalid token!')
  else:
    session = vk.AuthSession(access_token= token)
    api = vk.API(session, v='5.35', lang='en', timeout=10)
```

Функция для получения информации о конкретном пользоватле (добровольно указанных на его странице) по id (только цифры) с помощью метода **.users.get()** и запись её в файл:
```Python
def get_info(id):
  id = str(id)
  if id.isdigit():
    mas = api.users.get(user_ids=id, fields= 'online, last_seen, bdate, counters, domain, country, city')
    with open('users_info.txt', 'a') as f:
       a, b = id, str("{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
       f.write(f'==== Получение информации о пользователе с id = {a} | дата-время:{b} === \n')
       json.dump({"user_info": mas}, f, indent=4, ensure_ascii=False)
       f.write('\n')
  else:
    print('id пользователя состоит только из цифр!')
```

Результат: 
```Python
==== Получение информации о пользователе с id = 208608238 | датавремя:2018-11-23 18:07:56 === 
{
    "user_info": [
        {
            "id": 208608238,
            "first_name": "Kirill",
            "last_name": "Skorobogatov",
            "domain": "skorking",
            "bdate": "6.3.1998",
            "city": {
                "id": 2,
                "title": "Saint Petersburg"
            },
            "country": {
                "id": 1,
                "title": "Russia"
            },
            "online": 0,
            "last_seen": {
                "time": 1542995129,
                "platform": 4
            },
            "counters": {
                "albums": 26,
                "videos": 0,
                "audios": 1120,
                "notes": 0,
                "photos": 5160,
                "groups": 74,
                "gifts": 302,
                "friends": 108,
                "online_friends": 25,
                "user_photos": 1,
                "posts": 276,
                "subscriptions": 0,
                "pages": 49
            }
        }
    ]
}
```

Получение id и типа аккаунта по username:
```Python
def get_type_and_id(name):
  with open('get_type_and_id.txt', 'a') as f:
       a = name
       b = str("{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
       f.write(f'==== Определение id и type по username = {a} | дата-время:{b} === \n')
       result = api.utils.resolveScreenName(screen_name=name)
       json.dump(result, f, indent=4, ensure_ascii=False)
       f.write('\n')
```

Вывод:
```Python
==== Определение id и type по username = skorking | дата-время:2018-11-23 19:00:19 === 
{
    "type": "user",
    "object_id": 208608238
}
```

Функция для отправки сообщения пользователю на указанный id с использованием метода **.messages.send()** c прикреплённым файлом, в данном случае фотографией. Текст сообщения берётся из отдельного файла *message_text.txt*
```Python
def send_message(id):
  with open('message_text.txt', 'r') as f:
    text = ''
    for line in f:
      text+=line
  api.messages.send(user_id=str(id), message=text, attachment = 'photo208608238_456242857')
  print("Сообщение отправлено!")
```

Результат:

![python.png](https://github.com/python-advance/sem5-oop-Yalkinzsun/blob/master/%D0%92%D0%B0%D1%80%D0%B8%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B0%D0%BC%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/3.4/python1.png)

Просмотр истории n-сообщений с конца для id аккаунта, с которым велась переписка. Использовался метод **.messages.getHistory()**

```Python
def messages_history(id,number):
  history = api.messages.getHistory(count=number, user_id=str(id), start_message_id = -1)
  with open('history.txt', 'a') as f:
       a,b = str(number),str(id)
       c = str("{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
       f.write(f'Получения последних {a} сообщений диалога с пользователем с id = {b} | дата-время:{c} \n')
       json.dump(history, f, indent=4, ensure_ascii=False)
       f.write('\n')
```

Результат: 
```Python
Получения последних 3 сообщений диалога с пользователем с id = 208608238 | дата-время:2018-11-23 19:01:15 
{
    "count": 333,
    "items": [
        {
            "id": 214075,
            "body": "Третье сообщение",
            "user_id": 208608238,
            "from_id": 208608238,
            "date": 1542999592,
            "read_state": 1,
            "out": 0
        },
        {
            "id": 214074,
            "body": "Второе сообщение",
            "user_id": 208608238,
            "from_id": 208608238,
            "date": 1542999586,
            "read_state": 1,
            "out": 0
        },
        {
            "id": 214073,
            "body": "Первое сообщение",
            "user_id": 208608238,
            "from_id": 208608238,
            "date": 1542999580,
            "read_state": 1,
            "out": 0
        }
    ]
}
```

Функция просмотра количества лаков определённой фотографии и id лайкнувших пользователей c помощью метода **.likes.getList()** : 
```Python
def get_photo_likes(id_owner, id_item):
  likes = api.likes.getList(type='photo', owner_id=str(id_owner), item_id=str(id_item))
  with open('likes.txt', 'a') as f:
     a,b = str(id_owner),str(id_item)
     c = str("{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
     f.write(f'Кол-во лайков фотографии с id = {b} пользователя с id = {a} + список id-лайкнувших | дата-время:{c} \n')
     json.dump(likes, f, indent=4, ensure_ascii=False)
     f.write('\n')
```

Результат:

```Python
Кол-во лайков фотографии с id = 456251564 пользователя с id = 34045589 + список id-лайкнувших | дата-время:2018-11-23 18:56:33 
{
    "count": 60,
    "items": [
        7920505,
        498245675,
        227029873,
        ...
        48916669,
        157002424,
        69488120,
        134193253
    ]
}
```
