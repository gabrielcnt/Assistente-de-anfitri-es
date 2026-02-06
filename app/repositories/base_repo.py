
class BaseRepository:
    def __init__(self, db):
        self.db = db

    def add(self, entity):
        self.db.add(entity)
        return entity
    
    def delete(self, entity):
        self.db.delete(entity)

