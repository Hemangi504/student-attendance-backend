from flask import jsonify
from flask_jwt_extended import jwt_required
from app.main import app

@app.route('/api/admin/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({
        "status": True,
        "message": "Logout Successful"
    }), 200