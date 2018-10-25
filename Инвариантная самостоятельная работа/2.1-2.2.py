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

    def show(self):
        print("Date: " + str(self.date))
        print("Id: " + str(self.id))
        print("Author: " + str(self.author))
        print("Content: " + str(self._content))

    def show_comments(self):
        for comment in self.comments:
            comment.show()
            print()

class Comment(Post):
    def __init__(self, author, content):
        #используем метод __init__ суперкласса
        super(Comment, self).__init__(author=author, content=content)

if __name__ == "__main__":
    post = Post("Adam von Krusenstern", "It's the content", "Saint Petersburg")
    post.add_comment(Comment("Egor", "One, two, three, I'm a princess"))
    post.add_comment(Comment("Anka", "I'm crazy about cats ^^"))

    print("POST")
    post.show()
    print()
    print("COMMENTS")
    post.show_comments()
