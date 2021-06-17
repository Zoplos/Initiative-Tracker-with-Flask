from flask import Flask,render_template,request,redirect
from markupsafe import escape
import operator

app = Flask(__name__)
inputs = []
class Character:
    def __init__(self,roll,name,hp,ac):
        self.roll = roll
        self.name = name
        self.hp = hp
        self.ac = ac  

@app.route('/')
def index():
    return render_template("base.html") 

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return render_template("base.html") 
    if request.method == 'POST':
        roll = int(request.form['init'])
        name = request.form['name']
        hp = int(request.form['hp'])
        ac = int(request.form['ac'])
        inputs.append(Character(roll,name,hp,ac))
        sorted_inputs = sorted(inputs, key=operator.attrgetter("roll"))
        sorted_inputs = reversed(sorted_inputs)
        return render_template('data.html',inputs=sorted_inputs)

@app.route('/clear/', methods = ['POST', 'GET'])
def clear():
    inputs.clear()
    return render_template("base.html") 
        

