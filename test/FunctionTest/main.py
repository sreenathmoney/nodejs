from flask import jsonify, request, session
from rest import *
from dbconnector import *
from app import app

@app.route('/login1', methods=['POST'])
def login1():
    dbconnect()
   # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    if not request.is_json:
        return (jsonify({"msg": "Faild"}), 400, headers) 

    userAuthenticate =  Authenticate()

    return (jsonify(userAuthenticate) , 200, headers) 
#    [{'manish','kumar'},{'firstname','lastname'}]

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'

#start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)