from flask import Blueprint, jsonify, session
import sys

sys.path.append("..")
from controllers.playlist import get_user_playlist

user_blueprint = Blueprint('user', __name__, template_folder="templates")

@user_blueprint.route("/playlist/", methods=["GET"])
def user_playlist():
    playlist_names = get_user_playlist(session)
    return jsonify(playlist_names)