from eve import Eve
from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs


app = Eve()
Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/api/people/docs')
app.debug = True

# event hooks:
def pre_get_callback(resource, request, lookup):
    print 'A GET request on the "%s" endpoint has just been received!' % resource
app.on_pre_GET += pre_get_callback

# non-resource endpoints, see http://flask.pocoo.org/
@app.route("/hello/<thing>")
def hello(thing):
    return "Hello %s!" % thing

@app.route("/aws")
def aws():
    return "Something happened at AWS."

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
