import bottle
import os
import random

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff00',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data
    
    x = random.randint(1, 4)
    if(x = 1)
        return {
            'move': 'north',
            'taunt': 'battlesnake-python!'
        }
    elif(x = 2)
        return {
            'move': 'south',
            'taunt': 'battlesnake-python!'
        }
    elif(x = 3)
        return {
            'move': 'east',
            'taunt': 'battlesnake-python!'
        }
    else
        return {
            'move': 'west',
            'taunt': 'battlesnake-python!'
        }

    
    #return {
    #    'move': 'north',
    #    'taunt': 'battlesnake-python!'
    #}


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))