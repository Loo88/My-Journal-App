from flask import jsonify

def register_error_handlers(app):
    # Handling 404 errors
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not found"}), 404

    # Handling 400 errors (bad request)
    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify({"error": "Bad request"}), 400

    # Handling 500 errors (server errors)
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"error": "Internal server error"}), 500
