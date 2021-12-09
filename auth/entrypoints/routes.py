from flask import Blueprint

auth_routes = Blueprint("auth_route", __name__, url_prefix="/api/v1/auth")


@auth_routes.post("/user")
def create_user():
    return {"message": "user added successfully"}


@auth_routes.get("/user")
def get_user():
    return {"message": "user get successfully"}
