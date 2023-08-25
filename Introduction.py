from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text
from database import getProjectsFromDB
from database import getProjectsFromDB

app = Flask(__name__)

print(app)



@app.route('/')
def welcome():

# Getting projects from the database
    db_projects = getProjectsFromDB()
    return render_template('home.html', 
                           my_projects = db_projects,
                           owner_name = "Josaya 01")


# adding current projects in the route
@app.route('/api/projects')
def current_projects():
    return jsonify(getProjectsFromDB())

if __name__ == '__main__':
    app.run('0.0.0.0', debug = True)

