from sqlalchemy import create_engine, text
from flask import jsonify
import os
import urllib

# print(os.getcwd())

root_dir = os.getcwd()


# Getting certificate path
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file == "cert.pem":
            certificate_path = os.path.join(root, file)



db_connection_string = "mysql+pymysql://i5phka3xjg1vgctbiflg:pscale_pw_m11owQ518QL8JAzwI7LMAcuCsDOb4ufUqlpOYPr4hT4@aws.connect.psdb.cloud/dream_book?charset=utf8mb4"


engine = create_engine(db_connection_string,
                       connect_args={
                            "ssl": {
                                "ca": certificate_path
                            }
                        })

def getProjectsFromDB():
    with engine.connect() as conn:
        result = conn.execute(text("select * from dream_book"))

        projectList = []

        # looping through all the rows in the dream_book table
        for row in result.all():

            # converting results into a dictionary
            # _mapping maps every row data with the column name
            p_list = dict(row._mapping)

            # appending/adding every row result into a list
            projectList.append(p_list)

        print("my_projects_list",projectList)

        # returning the list
        return projectList
    











