from flask import Flask,url_for,request,render_template,jsonify
from flask_bootstrap import Bootstrap
import json
import spacy
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/analyze',methods=['GET','POST'])
def analyze():
	
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		# Analysis
		docx = nlp(rawtext)
		# Tokens
		custom_tokens = [token.text for token in docx ]
		# Word Info
		custom_wordinfo = [(token.text,token.lemma_,token.shape_,token.is_alpha,token.is_stop) for token in docx ]
		custom_postagging = [(word.text,word.tag_,word.pos_,word.dep_) for word in docx]
		# NER
		custom_namedentities = [(entity.text,entity.label_)for entity in docx.ents]
		# allData = ['Token:{},Tag:{},POS:{},Dependency:{},Lemma:{},Shape:{},Alpha:{},IsStopword:{}'.format(token.text,token.tag_,token.pos_,token.dep_,token.lemma_,token.shape_,token.is_alpha,token.is_stop) for token in docx ]
		allData = [('"Token":"{}","Tag":"{}","POS":"{}","Dependency":"{}","Lemma":"{}","Shape":"{}","Alpha":"{}","IsStopword":"{}"'.format(token.text,token.tag_,token.pos_,token.dep_,token.lemma_,token.shape_,token.is_alpha,token.is_stop)) for token in docx ]

		result_json = json.dumps(allData, sort_keys = False, indent = 2)

	return render_template('index.html',ctext=rawtext,custom_tokens=custom_tokens,custom_postagging=custom_postagging,custom_namedentities=custom_namedentities,custom_wordinfo=custom_wordinfo,result_json=result_json)

import wikipedia
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
from spacy import displacy

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

from flaskext.markdown import Markdown

Markdown(app)

@app.route('/search')
def display():
	return render_template('display.html')


@app.route('/extract',methods=["GET","POST"])
def extract():
	if request.method == 'POST':
		search1 = request.form['rawtext']
		summarizer = {}
		for items in wikipedia.search("\""+ search1 + "\"", results = 5):
			summarizer[items] = wiki_wiki.page(items).summary
		
		res = ''.join(key +"\n" +str(val) for key, val in summarizer.items())

		docx = nlp(res)
		html = displacy.render(docx,style="ent")
		html = html.replace("\n\n","\n")
		result = HTML_WRAPPER.format(html)

	return render_template('result.html',rawtext=res,result=result)


# API Routes
@app.route('/api')
def basic_api():
	return render_template('restfulapidocs.html')

# API FOR TOKENS
@app.route('/api/tokens/<string:mytext>',methods=['GET'])
def api_tokens(mytext):
	# Analysis
	docx = nlp(mytext)
	# Tokens
	mytokens = [token.text for token in docx ]
	return jsonify(mytext,mytokens)

# API FOR LEMMA
@app.route('/api/lemma/<string:mytext>',methods=['GET'])
def api_lemma(mytext):
	# Analysis
	docx = nlp(mytext.strip())
	# Tokens & Lemma
	mylemma = [('Token:{},Lemma:{}'.format(token.text,token.lemma_))for token in docx ]
	return jsonify(mytext,mylemma)

# API FOR NAMED ENTITY
@app.route('/api/entities/<string:mytext>',methods=['GET'])
def api_entities(mytext):
	# Analysis
	docx = nlp(mytext)
	# Tokens
	mynamedentities = [(entity.text,entity.label_)for entity in docx.ents]
	return jsonify(mytext,mynamedentities)

# API FOR MORE WORD ANALYSIS
@app.route('/api/data/<string:mytext>',methods=['GET'])
def data(mytext):
	docx = nlp(mytext.strip())
	allData = ['Token:{},Tag:{},POS:{},Dependency:{},Lemma:{},Shape:{},Alpha:{},IsStopword:{}'.format(token.text,token.tag_,token.pos_,token.dep_,token.lemma_,token.shape_,token.is_alpha,token.is_stop) for token in docx ]
	
	return jsonify(mytext,allData)
	
if __name__ == '__main__':
	app.run(debug=True)