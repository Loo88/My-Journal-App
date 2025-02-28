from flask import Flask, jsonify, request

def routes(app):
    #route for getting journal entries
    @app.route('/entries', methods=['GET'])
    def get_entries():
        #simulate fetching entries from a database
        entries = ['entry 1', 'entry 2']
        return jsonify({'entries': entries})

    #route for adding new journal entries
    @app.route('/entries', methods=['POST'])
    def add_entry():
        new_entry = request.json.get('entry')
        if not new_entry:
            return jsonify({'error': 'No entry provided'}), 400 #custom error if no entry is given
        #simulate adding the entry to a database
        return jsonify ({'message':'Entry added successfully'}), 201


