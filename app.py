from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    request,
)
from flask_cors import CORS
import logging
import sys
from helpers import get_toxicity
from scrape import get_posts_text

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route("/test")
def api_root():
    resp = jsonify(
        {u"statusCode": 200, u"status": "Up", u"message": u"Welcome to toxicity Detection api"}
    )
    resp.status_code = 200
    return resp

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def showToxicity():
    if request.method == "POST":
        keyword = request.form['text']
        print(keyword)
        print('scraping ...')
        post_list = get_posts_text(keyword)
        print('scraping ok \n')
        print('get toxicity ...')
        list_toxi = get_toxicity(post_list)
        return render_template('index.html', jsnObj=list_toxi)

if __name__ == '__main__':
  app.run(debug=True)