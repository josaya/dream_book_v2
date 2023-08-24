from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

print(app)

# projects = [
#     {
#         'id':1,
#         'Name': 'Stay Here',
#         'Description': 'Property finder app',
#         'Progress' : '60%'
#     },
#     {
#         'id':2,
#         'Name': 'Property Plus',
#         'Description': 'Property management app',
#         'Progress' : '99%'
#     },
#     {
#         'id':3,
#         'Name': 'Bucket List',
#         'Description': 'Fun activity planner and manager',
#         'Progress' : '25%'
#     },
#     {
#         'id':4,
#         'Name': 'Events Pro',
#         'Description': 'Events planner and manager',
#         'Progress' : '15%'
#     },
#     {
#         'id':5,
#         'Name': 'Learning Python',
#         'Description': 'Learning web development using Python'
#     }

# ]

def getProjectsFromDB():
    with engine.connect() as conn:
        result = conn.execute(text("select * from dream_book"))

        projectList = []

        for row in result.all():
            p_list = dict(row._mapping)
            projectList.append(p_list)

        print("my_projects_list",projectList)
        return projectList



@app.route('/')
def welcome():

# Getting projects from the database
    db_projects = getProjectsFromDB()
    print("my_projects_list2", db_projects)
    return render_template('home.html', 
                           my_projects = db_projects,
                           owner_name = "Josaya 01")


# adding current projects in the route
@app.route('/api/projects')
def current_projects():
    return jsonify(getProjectsFromDB())

if __name__ == '__main__':
    app.run('0.0.0.0', debug = True)

