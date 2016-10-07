class Post(object):


    def __init__(self, author, title, content,
                    post_date, likes, upvotes, comments, rank, code, post_id=None):


        self.author = author
        self.title = title
        self.content = content
        self.post_date = post_date
        self.likes = likes
        self.title = title
        self.upvotes = upvotes
        self.comments = comments
        self.rank = rank
        self.code = code
        self.post_id = uuid.uuid4().hex if post_id is None else post_id
