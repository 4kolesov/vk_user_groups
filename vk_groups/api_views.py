from flask import request, jsonify

from . import app, db
from .models import Group

from vk_services import get_user_groups_with_friends



@app.route('/api/groups/', methods=['GET'])
def get_groups(id):
    user_id = request.args.get('user_id')
    query = request.args.get('query')
    friends = request.args.get('friends')
    if friends and friends != '':
        groups = get_user_groups_with_friends(user_id)
        # возвратить список групп
        pass
    # получить группы, сохранить их в базу, вернуть группы
    pass


@app.route('/api/all_groups/', methods=['GET'])
def get_all_groups():
    groups = Group.query.all()
    results = [group.to_dict() for group in groups]
    return jsonify({'opinion': results}), 200
    pass
