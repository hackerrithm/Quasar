class blog(object):
    """description of class"""

    def __init__(self, author, title, content,
                    published_date, code, blog_id=None):


        self.author = author
        self.title = title
        self.content = content
        self.published_date = published_date
        self.code = code
        self.blog_id = uuid.uuid4().hex if blog_id is None else blog_id
