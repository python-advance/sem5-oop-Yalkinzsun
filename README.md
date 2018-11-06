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
