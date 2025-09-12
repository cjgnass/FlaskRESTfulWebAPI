from flask import Flask, request, jsonify
app = Flask(__name__)

class Sheet(object):
    def __init__(self):
        self.names = []

    def add(self, name):
        self.names.append(name)

    def delete(self, name):
        self.names.remove(name)

    def list(self):
        return self.names


sheet = Sheet()

@app.route('/')
def index():
    return 'welcome'

@app.route('/sheet/signup', methods=['POST'])
def signup():
    try:
        print(request)
        if 'name' in request.args:
            sheet.add(request.args['name'])
            return request.args['name'] + ' added successfully'
        else:
            raise Exception
    except:
        return 'no name given', 400

@app.route('/sheet/delete', methods=['DELETE'])
def delete():
    try:
        if 'name' in request.args:
            sheet.delete(request.args['name'])
            return request.args['name'] + ' deleted successfully'
        else:
            raise Exception
    except:
        return 'no name given', 400

@app.route('/sheet/list', methods=['GET'])
def list():
    return jsonify(sheet.list())



if __name__ == '__main__':
    app.run()

