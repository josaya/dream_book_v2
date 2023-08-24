from sqlalchemy import create_engine, text
from flask import jsonify
import os

# print(os.getcwd())

root_dir = os.getcwd()


# Getting certificate path
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file == "cert.pem":
            certificate_path = os.path.join(root, file)


db_connection_string = "mysql+pymysql://9obuxu48zm2gcooyrqqp:pscale_pw_xNzX8sE0jrf20x2jgGlpB7RDSgODgNIXpm4gz4nxX0l@aws.connect.psdb.cloud/dream_book?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={
                            "ssl": {
                                "ca": certificate_path
                            }
                        })

# with engine.connect() as conn:
#     result = conn.execute(text("select * from dream_book"))

#     projectList = []

#     for row in result.all():
#         p_list = dict(row._mapping)
#         projectList.append(p_list)


# print("projects list", projectList)
    











