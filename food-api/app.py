from crypt import methods, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:!@localhost/recipe'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    
    def __repr__(self):
        return f"User: {self.name}"

    def __init__(self,name):
       self.name = name

def format_event(user):
    return {
        "name": user.name,
        "description":user.description
    }

@app.route('/user', methods=['POST'])
def create_event():
    name = request.json['name']
    user = User(name)
    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
