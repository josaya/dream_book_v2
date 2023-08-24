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


db_connection_string = "mysql+pymysql://mtcgw9l4sa2w2idxl2zs:pscale_pw_ynx3uIUWCPJGfHD4gn5haZTrH6bKA1S9YiXRYWTAx4S@aws.connect.psdb.cloud/dream_book?charset=utf8mb4"

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
    











