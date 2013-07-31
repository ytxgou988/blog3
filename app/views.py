from app import app, db
from flask import render_template, url_for, flash, session, request, g, redirect
from forms import PostForm
from models import User, ROLE_USER, ROLE_ADMIN, Post
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template("index.html",
            title = 'Home',
            posts = posts)

@app.route('/article/<art_id>')
def article(art_id):
    posts = Post.query.get(art_id)
    return render_template("article.html",
            title = posts.p_title,
            posts = posts)

@app.route('/post', methods = ['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(p_title = form.post1.data, p_content = form.post2.data, times = str(datetime.now()))
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    return render_template('post.html',
            title = "Post",
            form = form
            )
@app.route('/edit/<art_id>', methods = ['GET', 'POST'])
def edit(art_id):
    form =PostForm()
    article = Post.query.get(art_id)
    if form.validate_on_submit():
 #       post = Post(p_title = form.post1.data, p_content = form.post2.data, times= str(datetime.now()))
         
        article.p_title = form.post1.data
        article.p_content = form.post2.data
        db.session.commit()
        return redirect('/article/'+art_id)
    return render_template('edit.html',
            title = 'Edit   '+article.p_title,
            form = form,
            article = article)
@app.route('/delete/<art_id>')
def delete(art_id):
    article = Post.query.get(art_id)
    db.session.delete(article)
    db.session.commit()
    return redirect('/index')
    
@app.route('/about')
def about():
    return render_template("about_me.html",
            title = "About Me")
