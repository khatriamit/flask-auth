import validators
from flask import Blueprint, request, jsonify
from model.database import db, User
from werkzeug.security import check_password_hash, generate_password_hash

auth_routes = Blueprint("auth_route", __name__, url_prefix="/api/v1/auth")


@auth_routes.post("/user")
def create_user():
    full_name = request.json["full_name"]
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]

    if not validators.email(email):
        return jsonify({"error": "email not valid"}, 400)

    if User.objects.filter_by(email=email).first() is not None:
        return jsonify({"error": "email already exists"}, 400)

    if User.objects.filter_by(username=username).first() is not None:
        return jsonify({"error": "username already exists"}, 400)

    hash_pwd = generate_password_hash(password)
    user = User(full_name=full_name, username=username, email=email, password=hash_pwd)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "user get successfully"}), 201


@auth_routes.get("/user")
def get_user():
    return {"message": "user get successfully"}
