from flask.ext.wtf import Form, TextField, BooleanField, TextAreaField
from flask.ext.wtf import Required
class PostForm(Form):
    post1 = TextField('post1', validators = [Required()])
    post2 = TextAreaField('post2', validators = [Required()])

