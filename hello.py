from flask import Flask, request, render_template
import json

app = Flask(__name__)

# Load from template
def build_reposonse(speech_text, card_title, card_content):
    with open('templates/default_response.json') as response_file:
        response = json.load(response_file)

    response["response"]["outputSpeech"]["text"] = speech_text
    response["response"]["card"]["title"] = card_title
    response["response"]["card"]["content"] = card_content

    return json.dumps(response)

def process_request(request_data):
    # Process request_data here and
    # build a suitable response
    response = build_reposonse("speech", "card", "card_content")
    return response

# Default request handler
@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return process_request(request.data)
    else:
        return render_template('hello.html')

# In order to simplify debugging you can
# just visit /test to get an interface
# to submit sample json, just like in
# the alexa developers test panel
@app.route('/test')
def test_page():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
