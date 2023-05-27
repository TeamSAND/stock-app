from flask import Flask, request, render_template
import requests
from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__, static_folder='static')

ENDPOINT_URL = "https://us-central1-aiplatform.googleapis.com/ui/projects/my-finsent-model/locations/us-central1/endpoints/205806586487111680:predict"
HEADERS = {
    "Authorization": "Bearer ya29.a0AWY7CkkJLMPAHU3hIX1wXuMoBh6IISNDVJwnCV0Lyzs1OwQHXiXnN-_dKlpiEx4zEI98_sM723nUadTem_1OcfwmuYcmcB3etEaYLibtlqkI-xIN-Txs40PDhpfAsIo4ETekRwAmW_UteA233FjIjIxfTRuKxu4SO0WhaCgYKAb0SARASFQG1tDrptNC7FcXV1_DrMnl-E5z9YA0171",
    "Content-Type": "application/json"
}

cred = credentials.Certificate('finsentbysand-firebase.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def fetch_latest_news(company):
    news_ref = db.collection(company).document('1')
    news_doc = news_ref.get()
    if news_doc.exists:
        latest_news = news_doc.to_dict()
        return latest_news
    else:
        return None
    
@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    company = request.form['test_data']
    # test_data = "stock gain 5 %"
    latest_news = fetch_latest_news(company)
    if latest_news:
        test_data = latest_news.get('news')
        data = {
            "instances": {
                "mimeType": "text/plain",
                "content": test_data
            }
        }
    # print(test_data)
        response = requests.post(ENDPOINT_URL, headers=HEADERS, json=data)
        result = response.json()
        print(result)
        if 'predictions' in result:
            sentiment = result["predictions"][0]["sentiment"]
        else:
            return " Auth Token Error "
            # sentiment = 2 
        # print(sentiment)
        # sentiment = 0
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
    
    return "No data Exist for the given Company" 

# @app.route('/news/latest')

    

if __name__ == "__main__":
    app.run(debug=True)
