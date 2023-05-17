class Task:
    id = None
    title = None
    description = None
    checkbox = None
    color = None
    photos = None
    column_id = None

    def __init__(self, id, title, description, color, checkbox, photos, column_id):
        self.id = id
        self.title = title
        self.description = description
        self.color = color
        self.checkbox = checkbox
        self.photos = photos
        self.column_id = column_id