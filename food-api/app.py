from flask_bcrypt import Bcrypt
from flask import Flask, request,abort, jsonify, session
from flask_session import Session
from models import *
import redis  

app = Flask(__name__)
app.secret_key="awdhbauijdawuidahwuidbawuidabduiaw"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Lakers12630!@localhost/postgres'
app.config['SESSION_TYPE'] = "redis"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True

bcrypt = Bcrypt(app)
server_session = Session(app)

    

SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route("/@me")
def current_user():
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({"error":"Unauthorized"}), 401
    
    user = User.query.filter_by(id=user_id).first()

    return jsonify({
        "id":user.id,
        "email":user.email
    })
@app.route('/register', methods=["POST"])
def register_user():
    email = request.json["email"]
    password = request.json["password"]

    user_exists = User.query.filter_by(email=email).first() is not None
    if user_exists:
        return jsonify({"error": "User already exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password).decode('utf8')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id":new_user.id,
        "email":new_user.email
    })


@app.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    #check to see if user exists
    user = User.query.filter_by(email=email).first()
    
    if user is None:
        return jsonify({"error":"Unauthorized"}),401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error":"Unauthorized"}), 401

    session["user_id"] = user.id
    return jsonify({
        "id":user.id,
        "email":user.email
    })



if __name__ == "__main__":
   app.run(debug=True)
