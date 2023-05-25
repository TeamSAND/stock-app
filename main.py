from flask import Flask, request, render_template
import requests

app = Flask(__name__)

ENDPOINT_URL = "https://us-central1-aiplatform.googleapis.com/ui/projects/my-finsent-model/locations/us-central1/endpoints/205806586487111680:predict"
HEADERS = {
    "Authorization": "Bearer ya29.a0AWY7Ckkk406Q96EZRSz3De5G4hp2sUlbkM6I6g2AiYF-khtavZmCBUvcGKKrIX7mJ6aHY6rROeV16Uv3x-YGaJQqQyLwqh_z8Dxoe4J5bd3fDeljJM4DvwQ0OYrIHC590eNKGsp9O20_URF8PPKUN8Mmm4TtWMIurA0X_6waCgYKAcYSARASFQG1tDrpF11SKY_O70aj_54Ntv8xpg0174",
    "Content-Type": "application/json"
}

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    test_data = request.form['test_data']

    data = {
        "instances": {
            "mimeType": "text/plain",
            "content": test_data
        }
    }

    response = requests.post(ENDPOINT_URL, headers=HEADERS, json=data)
    result = response.json()
    print(result)
    sentiment = result["predictions"][0]["sentiment"]
    print(sentiment)
    if sentiment is not None and sentiment >= 2:
        compound1 = "2"
        sentiment_label = "positive"
    elif sentiment is not None and sentiment == 1:
        compound1 = "1"
        sentiment_label = "Neutral"
    else:
        compound1 = "0"
        sentiment_label = "negative"

    return render_template('form.html', final=compound1, test_data=test_data, sentiment=sentiment_label)

if __name__ == "__main__":
    app.run(debug=True)
