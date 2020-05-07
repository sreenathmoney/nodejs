from google.cloud import bigquery
from google.oauth2 import service_account
from dbconnector import *

global connection

def userAuthenticateDAL(username,password):
    # credentials = service_account.Credentials.from_service_account_file(
    # 'gcp-test-app-231526-d33933990d5b.json')
    # project_id = 'gcp-test-app-231526'
    # client = bigquery.Client(credentials= credentials,project=project_id)

    # password=hashlib.md5(password.encode())
    # with connection.connect() as conn:
        # Execute the query and fetch all results
    
    # for Production
    db=dbconnect()
    connection = db.raw_connection()
    # for Local
    # connection=dbconnect()
    cursor = connection.cursor()
    cursor.execute(
            "select count(*) from ksridigital.user where user_name=%s and user_password=%s",(username,'477c16eab2866205dd128cbe6a8d3341')
    )

    if cursor != 0:
        cursor.execute("select user_first_name,user_last_name from ksridigital.user where user_name=%s",(username))

    content = {}
    for row in cursor.fetchall():
        content = {'firstname': row[0], 'lastname': row[1]}
#     query = """
#     SELECT count(*) FROM `gcp-test-app-231526.UserInfo.Users` 
#     where UserName=@username and Password=@password 
#     LIMIT 1;
# """
#     job_config = bigquery.QueryJobConfig(   
#         query_parameters=[
#             bigquery.ScalarQueryParameter("username", "STRING", username),
#             bigquery.ScalarQueryParameter("password", "STRING", password),
#                     ]
#             )
#     query_job = client.query(query, job_config=job_config)
#     results = query_job.result() 
#     if results != 0:
#         query = """
#     SELECT firstName,lastName FROM `gcp-test-app-231526.UserInfo.Users` 
#     where UserName=@username 
#     LIMIT 1;
# """
#     job_config = bigquery.QueryJobConfig(   
#         query_parameters=[
#             bigquery.ScalarQueryParameter("username", "STRING", username),
#                     ]
#             )
#     query_job = client.query(query, job_config=job_config)
#     userresults = query_job.result() 


    return  content