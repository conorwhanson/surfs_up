from flask import Flask

app = Flask(__name__)

@app.route('/')

def welcome():
    """welcome homie
    """
    return(f"where you going?<br/>"
        f"/hello<br/>"
        f"/rose<br/>"
        )
@app.route('/hello')

def hello_world():
    return('Hello world')

@app.route('/rose')

def rose():
    return('a rose by any other name would be weird')

if __name__ == '__main__':
    app.run(debug=True)