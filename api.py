#import liberaries
from flask import Flask


#Create flask object
app = Flask(__name__)


#Creating route and function
@app.route('/home')
def index():
    return 'Home Page!'

@app.route('/about')
def about():
    return 'About Page!'

@app.route('/about/<string:name>/<int:quantity>')
def Custormername(name, quantity):
    return 'Your Custom Order:' + name + ': Quanity ' + (str(quantity))



#Running Python File
if __name__ == '__main__':
    app.run(debug=True)

