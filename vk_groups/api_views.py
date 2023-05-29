from flask import jsonify, request, url_for

from settings import TRUE_FLAGS
from vk_groups.vk_services import (get_groups_by_query,
                                   get_groups_user_by_query,
                                   search_group_with_friends)

from . import app, db
from .models import Group


@app.route('/api/groups/', methods=['GET'])
def get_groups():
    """
    Возвращает список групп VK по заданному запросу.
    ---
    parameters:
      - name: user_id
        in: query
        type: string
        required: true
        description: ID пользователя VK.
      - name: query
        in: query
        type: string
        required: true
        description: Запрос для поиска групп.
      - name: friends
        in: query
        type: string
        required: false
        description: Если указано "true", "True" или "1" — осуществляется поиск групп по подстроке, в которые входит пользователь и его друзья.
    responses:
      200:
        description: Результаты вернулись успешно
        examples:
          application/json: |
            {
              "results": [
                  {
                      "group_id": 696969,
                      "group_name": "Название группы 1"
                  },
                  {
                      "group_id": 999666,
                      "group_name": "Название группы 2"
                  },
                  ...
              ]
            }
      201:
        description: Результаты вернулись успешно
        examples:
          application/json: |
            {
              "results": [
                  {
                      "group_id": 123456,
                      "group_name": "Название группы 1"
                  },
                  {
                      "group_id": 789012,
                      "group_name": "Название группы 2"
                  },
                  ...
              ]
            }
      400:
        description: Произошла ошибка при запросе
        examples:
          application/json: |
            {
                "error": "user_id: \"000000asdasd\" должен быть числом!"
            }
    """
    user_id = request.args.get('user_id')
    query = request.args.get('query')
    if not user_id:
        return (
            jsonify({'error': 'Отсутстует user_id: ID пользователя VK'}),
            400,
        )
    if not query:
        return jsonify({'error': 'Отсутстует query: запрос.'}), 400
    if not user_id.isdigit():
        return (
            jsonify({'error': f'user_id: "{user_id}" должен быть числом!'}),
            400,
        )

    friends = request.args.get('friends')
    if friends in TRUE_FLAGS:
        results = search_group_with_friends(int(user_id), query)
        return jsonify({'results': results}), 200

    groups = get_groups_by_query(query)
    id_find_groups = get_groups_user_by_query(int(user_id), query)
    results = []
    for group in groups:
        if group.get('id') in id_find_groups:
            if (
                not db.session.query(Group)
                .filter_by(group_id=group.get('id'), query=query)
                .first()
            ):
                obj = Group(
                    query=query,
                    group_id=group.get('id'),
                    group_name=group.get('name'),
                )
                db.session.add(obj)
            results.append(
                dict(
                    group_id=group.get('id'),
                    group_name=group.get('name'),
                )
            )
    db.session.commit()
    return jsonify({'results': results}), 201


@app.route('/api/all_groups/', methods=['GET'])
def get_all_groups():
    """
    Возвращает все сохраненные группы из базы данных.
    ---
    parameters:
      - name: page
        in: query
        type: integer
        required: false
        default: 1
        description: Номер страницы.
      - name: per_page
        in: query
        type: integer
        required: false
        default: 10
        description: Количество элементов на странице.
    responses:
      200:
        description: Результаты вернулись успешно
        examples:
          application/json: |
            {
              "page": 1,
              "per_page": 10,
              "total_count": 100,
              "total_pages": 10,
              "prev_page": null,
              "next_page": "http://example.com/api/all_groups/?page=2&per_page=10",
              "results": [
                  {
                      "group_id": 123456,
                      "group_name": "Название группы 1"
                  },
                  {
                      "group_id": 789012,
                      "group_name": "Название группы 2"
                  },
                  ...
              ]
            }
      204:
        description: Нет данных для отоборажения
        examples:
          application/json: |
            {
                "error": "В базе данных отсутствуют экземпляры запросов."
            }
    """
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    objects = db.session.query(Group).paginate(
            page=page, per_page=per_page, error_out=False
        )
    total_count = objects.total
    if not total_count:
        return (
            jsonify({'error': 'В базе данных нет ни одного запроса!'}),
            204,
        )
    total_pages = objects.pages
    results = [obj.to_dict() for obj in objects]
    prev_page = url_for(
            'get_all_groups', page=page - 1, per_page=per_page, _external=True
        ) if page > 1 else None
    next_page = url_for(
            'get_all_groups', page=page + 1, per_page=per_page, _external=True
        ) if page < total_pages else None
    response = {
        'page': page,
        'per_page': per_page,
        'total_count': total_count,
        'total_pages': total_pages,
        'prev_page': prev_page,
        'next_page': next_page,
        'results': results,
    }
    return jsonify(response), 200
