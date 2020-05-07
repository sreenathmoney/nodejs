import pymysql
import sqlalchemy
import os
from flask import Flask
from app import app



global connection
def dbconnect():
        # Connect through locally URL
        DATABASE_URI='mysql+pymysql://root:12345@15@127.0.0.1:3306/ksridigital'
        # Connect through GCP URL
        # DATABASE_URI = 'mysql+pymysql://root:213213@15@/ksridigital?unix_socket=/cloudsql/gcp-test-app-231526:asia-east2:samanish'
        # DATABASE_URI=app.config.get("DATABASE_URI")
        db = sqlalchemy.create_engine(DATABASE_URI,pool_size=1,
            max_overflow=2,
            pool_timeout=30,
            pool_recycle=1800
        )

        # db = sqlalchemy.create_engine(
        # # Equivalent URL:
        # # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
        # sqlalchemy.engine.url.URL(
        #     drivername="mysql+pymysql",
        #     username="root",
        #     password="kanak@15",
        #     database="ksridigital",
        #     query={"unix_socket": "/cloudsql/{}".format("gcp-test-app-231526:asia-east2:samanish")},
        #     ),
        #     pool_size=1,
        #     max_overflow=2,
        #     pool_timeout=30,
        #     pool_recycle=1800
        # )
        # connection = pymysql.connect(host='127.0.0.1',
        #                                     db='ksridigital',
        #                                     user='root',
        #                                     password='kanak@15')
        # db_Info = connection.get_server_info()
        # print("Connected to MySQL Server version ", db_Info)
        # cursor = connection.cursor()
        # cursor.execute("select database();")
        # record = cursor.fetchone()
        # print("You're connected to database: ", record)
        return db
