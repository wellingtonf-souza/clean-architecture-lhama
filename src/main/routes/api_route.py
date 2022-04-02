from flask import Blueprint, jsonify

# from src.main.composer import register_user_composer

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/status", methods=["GET"])
def status():
    """Status APP"""
    return jsonify({"status": 200})
