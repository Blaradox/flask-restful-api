#!/usr/bin/env python3

import json
from flask import Flask, request, jsonify

# setup flask to use this file
app = Flask(__name__)

# single test route to run every_three_letters function
@app.route('/test', methods=['POST'])
def every_three_letters():
    # get data from post request
    data = json.loads(request.data)
    string_to_cut = data['string_to_cut']
    # change input string to array
    str_list = list(string_to_cut)
    # select third letter in array and every 3 letter after that
    every_three_list = str_list[2::3]
    # change array back to string
    result = ''.join(every_three_list)
    # return result as a json object
    return json.dumps({'return_string': result})

if __name__ == '__main__':
    app.run(debug=True)
