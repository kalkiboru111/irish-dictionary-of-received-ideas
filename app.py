import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'irish_dictionary'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')

# View directs user to terms page
@app.route('/get_terms')
def get_terms():
    return render_template("terms.html", 
    terms=mongo.db.terms.find())

@app.route('/add_term')
def add_term():
    return render_template("add_term.html", 
    categories=mongo.db.categories.find())

@app.route('/insert_term', methods=['POST'])
def insert_term():
    terms = mongo.db.terms
    terms.insert_one(request.form.to_dict())
    return redirect(url_for('get_terms'))
    
@app.route('/edit_term/<term_id>')
def edit_term(term_id):
    the_term =  mongo.db.terms.find_one({"_id": ObjectId(term_id)})
#    all_categories =  mongo.db.categories.find()
    all_categories = []
   
    print(mongo.db)
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

@app.route('/delete_term/<term_id>')
def delete_term(term_id):
    mongo.db.terms.remove({"_id": ObjectId(term_id)})
    return redirect(url_for('get_terms'))

@app.route('/get_categories')
def get_categories():
    return render_template("categories.html", 
    categories=mongo.db.categories.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)