from eve import Eve
from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs

app = Eve()
Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/api/people/docs')

app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
