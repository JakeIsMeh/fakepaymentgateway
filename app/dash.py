import shelve
from flask import Blueprint, render_template

bp = Blueprint('dash', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    s = shelve.open('instance/storage.db', flag='c')
    db = {}

    try:
        db = s['db']
    except KeyError:
        print('db not found')
    
    # reverse key order
    db = dict(reversed(list(db.items())))

    return render_template('dash.html', db=db)