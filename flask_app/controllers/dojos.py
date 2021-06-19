from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojo import Dojo
# from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result/<int:id>')
def submitted(id):
    dojos = Dojo.get_one({'id':id})
    return render_template("show.html",dojos=dojos)

@app.route('/process',methods=['POST'])
def create_user():
    # if not True or validate returns false... redirect to form
    if not Dojo.validate_user(request.form):
        return redirect('/')
    data = {
        'name':request.form['full_name'],
        'location':request.form['location'],
        'language':request.form['language'],
        'comment':request.form['comment']
    }
    
    id = Dojo.insert(data)
    print(f"The ID is: ====   {id}")
    return redirect(f"/result/{id}")