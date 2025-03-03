from flask import Flask, jsonify, request
from google.cloud import speech

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
    
    #route for transcribing speech
    @app.route('/transcribe', methods=['POST'])
    def transcribe_audio_local():

        #create client for speech to text API
        client = speech.SpeechClient()

        audio_file = request.files['audio']

        #create variable to store the content of the uploaded audio file
        content = audio_file.read()

        #create object which holds the audio data which is to be sent to the API using the content variable above
        audio = speech.RecognitionAudio(content=content)

        #define configuration settings for audio transcript
        config = speech.RecognitionConfig (
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code="en-US",
        )

        #send audio and configuration to API for processing
        response = client.recognize(config=config, audio=audio)

        #initialise empty list to hold audio transcript
        transcripts = []

        #iterate over transcrition results and use the most likely (1st) one
        for result in response.results:
            transcripts.append(result.alternatives[0].transcript)

        #return json response containing transcripts list
        return jsonify ({'transcripts': transcripts})

