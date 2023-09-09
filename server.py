
import random
import os
from flask import Flask, request, jsonify
from keyword_spotting_serviec import Keyword_Spotting_Service
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


AUDIO_OUTPUT_FILENAME = "waveOutPut\output.wav"
# instantiate flask app


@app.route("/SpeechRecognize", methods=["POST"])
def SpeechRecognize():
 # get file from POST request and save it
 audio_file = request.files["file"]
 file_name = str(random.randint(0, 100000))
 audio_file.save(file_name)
 # instantiate keyword spotting service singleton and get prediction
 kss = Keyword_Spotting_Service()
 predicted_keyword = kss.predict(file_name)
 # we don't need the audio file any more - let's delete it!
 os.remove(file_name)

 # send back result as a json file
 #result = {"keyword": predicted_keyword}
 return jsonify({'result':predicted_keyword} )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
     
    file = open(AUDIO_OUTPUT_FILENAME, "rb")
     
    # package stuff to send and perform POST request
    #response = requests.post(URL, files=values)
