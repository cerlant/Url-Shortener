from app import db
from app.base62 import to_base

BASE_HASH = 100000

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), unique=True)
    url_hash = db.Column(db.String(128, ), unique=True)

    def __repr__(self):
        return '<Data id:{}, url_hash: {}, url: {}>'.format(self.id, self.url_hash, self.url)

    def short_url(self):
        hash_string = to_base(BASE_HASH + self.id)
        self.url_hash = hash_string

    def get_url_shortened(self):
        return self.url_hash