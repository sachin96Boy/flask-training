from db import db

class StoreModel(db.Model):
    # define table name for sqlAlchemy
    __tablename__ = 'stores'

    # definr table columns for sqlAlchaney
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # back referenece to the item model
    # lazy='dynamic' means that it will not create an object for each item
    # it will only create an object when we call json method
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        # sotre and items share an one to many relationship
        # so we can use the back reference to get all the items
        # that belong to this store
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1


    def save_to_db(self):
        # session is a collection of objects that we're going to write to the database
        db.session.add(self)
        db.session.commit()
    

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    
