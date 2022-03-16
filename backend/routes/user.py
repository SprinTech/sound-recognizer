from flask import Blueprint, jsonify, session, jsonify
import sys

sys.path.append("..")
from controllers.playlist import get_user_playlist
from controllers.user import get_users, get_user

user_blueprint = Blueprint('user', __name__, template_folder="templates")

@user_blueprint.route("/user/", methods=["GET"])
def user_list():
    user_list = get_users()
    return jsonify(user_list)

@user_blueprint.route("/user/<string:username>", methods=["GET"])
def user_by_username(username):
    user = get_user(username)
    return jsonify(user)

@user_blueprint.route("/playlist/", methods=["GET"])
def user_playlist():
    playlist_names = get_user_playlist(session)
    return jsonify(playlist_names)