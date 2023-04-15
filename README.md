# Stock Sentiment Analysis from News headlins

 Platform that uses Google Cloud's natural language processing and AMD instances to analyze and categorize financial news articles and social media posts, providing personalized investment recommendations for individuals. 

## Overview: 

Once decision is made, the project allows one to go out to a historical ticker source to see if the action yielded any profits. Sentiment analysis is a technique used to identify and extract subjective information from textual data. It is used to analyze opinions, attitudes, and emotions expressed in text. Sentiment analysis is widely used in the fields of marketing, customer service, and social media monitoring. 

 

**Project consists of three packages:** 

**1. Finacial sites and related parsing** 

Goes out to sites like money control and listens on interesting news from Reuters via the Python Python library that is Beautiful Soup 

Also Create a data Frame using pandas library and create a CSV file. 

The news is captured and written to output. 

**2. Sentiment**  

The sentiment analysis takes the input from Python Script as a CSV file and looks up the sentiment using a sentiment analysis API 

Based on the score back from the API, we will make a decision to execute or not 

**3. Stock analyzer** 

After that, we will train and test the AutoMl model and send the result as a API for website deployment. We will query a finance API just after executing the query.  

If we decided to previously buy the stock (based on a positive sentiment) and there is an increase in the stock price, we are in profit and vice-versa and show the Positive Negative and Neutral sentiment on web page... 

# Installation: 

Install Python 3.x from the official website   `https://www.python.org/downloads/ `

Install Beautiful Soup by opening a command prompt or terminal and typing the following command: `pip install BeautifulSoup `

Install Pandas by opening a command prompt or terminal and typing the following command: `pip install pandas` 

Install NumPy by opening a command prompt or terminal and typing the following command: `pip install NumPy `
___

Clone the repository: 
```
git clone https://github.com/username/stock-app.git
```
Navigate into the cloned repository:

```
cd stock-app
```


Create a virtual environment:
```
python3 -m venv venv
```

Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```

On Unix or Linux:

```
source venv/bin/activate
```

Install the required dependencies:

```
pip install -r requirements.txt
```

Set the Flask application environment variable:

On Windows:
```
set FLASK_APP=main.py
```
On Unix or Linux:
```
export FLASK_APP=main.py
```

Run the Flask application using the flask run command:
```
flask run
```

Alternative Way, Run 
```
python main.py
```

Open your web browser and visit http://127.0.0.1:5000/ to see the Flask application running.
___
  

Usage: 


Install Python 3.x from the official website   `https://www.python.org/downloads/ `

Install Beautiful Soup by opening a command prompt or terminal and typing the following command: `pip install BeautifulSoup `

Install Pandas by opening a command prompt or terminal and typing the following command: `pip install pandas` 

Install NumPy by opening a command prompt or terminal and typing the following command: `pip install NumPy`


```

Load the dataset into a Pandas datagram. 

Preprocess the text data by removing unwanted characters, converting text to lowercase, and removing stop words. 

Use AutoMl to build a machine learning model to classify the reviews as positive, negative or neutral. 

Evaluate the performance of the model using metrics such as accuracy, precision, recall, and F1-score. 

Use the trained model to predict the sentiment of new reviews. 

README file for Stock Market Prediction Analyzer using Google Cloud AMD Instance
```

Requirements: 

Google Cloud account 

AMD instance on Google Cloud 

Python 3.x 

Pandas 

Installation: 

Create a Google Cloud account if you don't have one already. 

Create an AMD instance on Google Cloud by following the instructions in the Google Cloud documentation. 

SSH into the instance and install Python 3.x by running the following command: `Sudo apt-get install python3 `

Install Pandas by running the following command: `pip3 install pandas `

Usage: 

Load the historical stock price data into a Pandas data Frame. 

Preprocess the data by removing unwanted columns and rows and normalizing the data. 

Split the data into training and testing sets. 

Use AutoMl to build a machine learning model to predict the stock prices. 

Deploy The Model on AMD instance by VM instance to visualize the predicted prices and actual prices. 

Note: 

Make sure to store sensitive information such as API keys and passwords in a secure manner, and do not share them in code or publicly. Also, make sure to follow Google Cloud security best practices to prevent unauthorized access to your instance and data. 




 

 
