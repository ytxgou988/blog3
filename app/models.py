from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default = ROLE_USER )
    posts = db.relationship('Post', backref = 'user', lazy = 'dynamic' )

    def __init__(self, name, password):
        self.name = name
        self.password = password
        

    def __repr__(self):
        return '<User %r>' % (self.name)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    p_title = db.Column(db.String(64), index = True)
    p_content = db.Column(db.String(1024))
    times = db.Column(db.String(64))
    author = db.relationship("User", backref=db.backref('post', order_by=id))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r user_id %d>' % (self.title, self.user_id)


