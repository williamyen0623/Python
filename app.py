from flask import Flask
app = Flask(__name__)

@app.route('/home')
@app.route('/data/appInfo/FlaskSE', methods=['GET'])
@app.route('/data/appInfo/id/5', methods = ['GET'])

def home():
    return "hello flask"


if __name__=="__main__":
    app.run()

def queryDataMessageByName(FlaskSE):
    print("type(name) : ", type(FlaskSE))
    return 'String => {}'.format(FlaskSE)

def queryDateMesageById(id):
    print("type(id):", type(id))
    return 'int => {}'.format(id)
