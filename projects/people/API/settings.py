# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'dev'
MONGO_PASSWORD = 'devpass'
MONGO_DBNAME = 'devdb'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Disable concurrency control
IF_MATCH = False

# Disable HATEOAS (Hypermedia as the Engine of Application State)
HATEOAS = False

schema_people = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'email': {
        'type': 'string',
        'minlength': 4,
        'maxlength': 50,
        'required': True,
        # this is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'born': {
        'type': 'datetime',
    },
}

people = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<login>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'email'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],
    
    # After all, not forcing normalized information is one of the selling points 
    # of MongoDB and many other NoSQL data stores.
    # 'allow_unknown': True,

    'schema': schema_people
    
}

DOMAIN = {
    'people': people,
}