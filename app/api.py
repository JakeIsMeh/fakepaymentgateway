import shelve
import requests

from .order  import Order
from flask import Blueprint, request, redirect, url_for, current_app

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/add', methods=['GET'])
def addOrder():
    ref = request.args.get('ref')
    amt = request.args.get('amt')
    method = request.args.get('method')

    s = shelve.open('instance/storage.db', flag='c')
    db = {}

    try:
        db = s['db']
    except KeyError:
        print('db not found')
    finally:
        db[ref] = Order(ref, amt, method, 'Pending')
        
        s['db'] = db
        s.close()

    return ('', 200)


@bp.route('/<ref>/<action>')
def approveOrder(ref, action):
    print(action)

    if action != 'approve' and action != 'deny':
        return ('Unknown action', 400)

    if action == 'approve':
        action = 'approved'
    elif action == 'deny':
        action = 'denied'

    s = shelve.open('instance/storage.db', flag='c')
    db = {}

    try:
        db = s['db']
    except KeyError:
        print('db not found')
        s.close()
        return ('Database Error', 500)
    
    try:
        order = db[ref]
    except KeyError:
        print('order doesnt exist')
        s.close()
        return ('Order not found', 404)
    
    payload = {'ref': ref, 'status': action}
    r = requests.get(current_app.config['ENDPOINT'], params=payload)
    if r.status_code != 200:
        return('Unable to make request', 500)

    order.status = action
    db[ref] = order
    s['db'] = db

    s.close()

    return redirect(url_for('dash.index'))
