#!flask/bin/python
from flask import Flask
from flask import request, abort, json, jsonify
import ScholarshipFinder as sc

app = Flask(__name__)


# tests
sample_matrix = [[1, 2, 3, 4, 5],
                 [1, 1, 2, 3, 5],
                 [3, 4, 5, 5, 5],
                 [3, 4, 5, 9, 5],
                 [1, 1, 5, 5, 25]]

# print sc.find_max_scholarship(sample_matrix)  # expected result: [5, 5, 5, 5, 25]
# print sc.find_max_scholarship(sample_matrix, 3)  # expected result: [5, 9, 25]

@app.before_request
def only_json():
    if not request.is_json:
        abort(400)


@app.route('/max_scholarship', methods=['POST'])
def index():
    data = json.loads(request.data)['data']
    result = sc.find_max_scholarship(data)

    response = jsonify(result)
    response.status_code = 200

    return response

if __name__ == '__main__':
    app.run(debug=True)
