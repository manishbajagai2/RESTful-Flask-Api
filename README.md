# RESTful-Flask-Api

An api to collect data from Wikipedia. Made entirely using Python and Flask. This can perform NER or Name Entity Recognition

# How to use the API

- To perform a quick outlook of the data and the data being processed, use the live url to go into the main page. Here in the input box, supply any sentence. When clicked on Submit, the result will be shown below which includes Tokens, Word Information, Named Entities and Part of Speech. 

- In the navigation bar choose the Wiki Search option to perform the NER and get data from the Wikipedia. In the input box, type in any valid keyword or sentence or phrase. When submitted, the api will make a post request to the Wikipedia Api. Doing so, the Flask Api will automatically process and fetch the top 5 search results. Finally the output is shown side to side in comparison to the annotated text using Spacy library.

- In the index page, if we choose the Api option of the navigation bar, we will be directed to a page where we can see how to use api in the default local server.However we can still tap into the live url for the nodemon to make a GET or the POST requests. The output would be shown in a JSON format in the browser itself.


## Features

- Show annotated text as well as the raw data collected from the wikipedia api.
- Customize our search and get different results
- Hosted online, so make a GET or a POST request anytime, also using Nodemon to verify
- Responsive to various devices.

## Dependencies

- Python>=3.8.7
- en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0-py3-none-any.whl
- Flask==1.1.2
- Flask-Bootstrap==3.3.7.1
- Flask-Markdown==0.3
- gunicorn==20.1.0
- jsonify==0.5
- jsonschema==3.2.0
- Markdown==3.3.4
- spacy==3.0.5
- wikipedia==1.4.0
- Wikipedia-API==0.5.4

## Live Project URL

https://flask-restful-wiki-api.herokuapp.com/
