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

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @name.getter
    def name(self):
        return self._name

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

    def show(self):
        print("Nickname: " + str(self.nickname))
        print("Name: " + str(self.name))
        print("Surname: " + str(self.surname))
        print("Email: " + str(self.email))
        print("Birthday: " + str(self.birthday))

if __name__ == "__main__":
    new_event = ITConference("Google I/O", "31/10/2018", "I/O brings together developers from around the globe annually for talks, hands-on learning with Google experts, and a first look at Google's latest developer product")
    new_event.add_member(Member("Ylki", "Kirill", "Skorobogatov", "Kirill@gmail.com", "06/03/1998"))
    new_event.add_member(Member("Spiderman", "Peter", "Parker", "spider@spiderweb.com", "01/01/0001"))

    print(">> Conference <<")
    new_event.show()
    print()
    print(">> Members <<")
    new_event.show_members()
