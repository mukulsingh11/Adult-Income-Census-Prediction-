from flask import Flask
from income.logger import logging

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

def index():
    logging.info('We are just testing the logging moduls')
    return 'Hello...  We are start the Adult Income Censun Prediction ML Project'

if __name__=='__main__':
    app.run(debug=True)

