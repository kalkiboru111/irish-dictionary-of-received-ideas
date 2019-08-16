import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, DESCENDING
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length 
from bson.objectid import ObjectId
import re
import os
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissecret!'

app.config['MONGO_DBNAME'] = 'irish_dictionary'
app.config["MONGO_URI"] = "mongodb+srv://root:83ZQythXiDEUTHCq@myfirstcluster-qstcj.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

#User Registration Form - taken from Pretty Printed github
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('register'))
        
        flash('That username already exists! Please choose another')

    return render_template('register.html')

#Login Form - taken from Pretty Printed github
@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users =mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})
        
        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('get_terms'))
            flash('Invalid username/password combination')
    return render_template('login.html')
    
#Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# Home - displays dictionary.
@app.route('/get_terms')
def get_terms():
    return render_template("terms.html", 
    terms=mongo.db.terms.find())
    
# Add Term - provides users with form to add terms.
@app.route('/add_term')
def add_term():
    return render_template("add_term.html", 
    categories=mongo.db.categories.find())

@app.route('/insert_term', methods=['POST'])
def insert_term():
    terms = mongo.db.terms
    terms.insert_one(request.form.to_dict())
    return redirect(url_for('get_terms'))

# Edit Term - provides users with form to edit terms.
@app.route('/edit_term/<term_id>')
def edit_term(term_id):
    the_term =  mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edit_term.html', term=the_term,
                           categories=all_categories)
                           
                           
@app.route('/update_term/<term_id>', methods=['POST'])
def update_term(term_id):
    terms = mongo.db.terms
    terms.update( {"_id": ObjectId(term_id)},
    {   'term_name':request.form.get('term_name'),
        'category_name':request.form.get('category_name'),
        'term_definition': request.form.get('term_definition'),
        'term_origin':request.form.get('term_origin')
    })
    return redirect(url_for('get_terms'))

#Vote functionality  
@app.route('/vote/<term_id>')
def vote(term_id):
    the_term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    return render_template('vote.html', the_term=the_term)

@app.route('/update_votes/<term_id>', methods=['POST'])
def update_votes(term_id):
    terms = mongo.db.terms
    totalVotes = mongo.db.terms.totalVotes()
    terms.update( {"_id": ObjectId(term_id)},
    {   'term_name':request.form.get('term_name'),
        'category_name':request.form.get('category_name'),
        'term_definition': request.form.get('term_definition'),
        'term_origin':request.form.get('term_origin'),
        'totalVotes': request.form.get('totalVotes')
    })
    return redirect(url_for('get_terms'), totalVotes=totalVotes)

# Delete Term - provides users with means to delete terms.
@app.route('/delete_term/<term_id>')
def delete_term(term_id):
    mongo.db.terms.remove({"_id": ObjectId(term_id)})
    return redirect(url_for('get_terms'))

# Categories - displays all categories.
@app.route('/get_categories')
def get_categories():
    return render_template("categories.html", 
    categories=mongo.db.categories.find())

# Edit Category - provides users with means to edit categories.
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one(
    {'_id': ObjectId(category_id)}))

@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))

# Delete Category - provides users with means to delete category.
@app.route('/delete__category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove(
        {'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))
    
@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')},
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))

#Add Category - provides users with means to add categories. 
@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')

#Search - provides users with means to text search through terms, categories and definitions.  
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    results = mongo.db.terms.find({ "$text": { "$search": query } } )
    return render_template( "search.html", results=results, query=query)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)