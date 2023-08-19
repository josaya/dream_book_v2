from flask import Flask, render_template, jsonify

app = Flask(__name__)

print(app)

projects = [
    {
        'id':1,
        'Name': 'Stay Here',
        'Description': 'Property finder app',
        'Progress' : '60%'
    },
    {
        'id':2,
        'Name': 'Property Plus',
        'Description': 'Property management app',
        'Progress' : '99%'
    },
    {
        'id':3,
        'Name': 'Bucket List',
        'Description': 'Fun activity planner and manager',
        'Progress' : '25%'
    },
    {
        'id':4,
        'Name': 'Events Pro',
        'Description': 'Events planner and manager',
        'Progress' : '15%'
    },
    {
        'id':5,
        'Name': 'Learning Python',
        'Description': 'Learning web development using Python'
    }

]

@app.route('/')
def welcome():
    return render_template('home.html', 
                           my_projects = projects,
                           owner_name = "Josaya 01")


# adding current projects in the route
@app.route('/api/projects')
def current_projects():
    return jsonify(projects)

if __name__ == '__main__':
    app.run('0.0.0.0', debug = True)

