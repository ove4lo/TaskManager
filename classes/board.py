class Board:
    id = None
    private = None
    title = None
    description = None
    user_id = None

    def __init__(self, id, private, title, description, user_id):
        self.id = id
        self.private = private
        self.title = title
        self.description = description
        self.user_id = user_id