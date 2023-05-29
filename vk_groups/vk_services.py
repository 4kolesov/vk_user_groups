import os
from typing import Any

import requests

from settings import VK_API_VERSION

ACCESS_TOKEN = os.getenv('VK_TOKEN')


def get_id_user_groups(user_id: int) -> list | None:
    """Возвращает список ID групп юзера."""
    URL = 'https://api.vk.com/method/groups.get'
    params = {
        'access_token': ACCESS_TOKEN,
        'v': VK_API_VERSION,
        'user_id': user_id,
    }

    response = requests.get(URL, params=params)
    if response.status_code == 200:
        data = response.json()
        groups = data.get('response', {}).get('items', [])
        return groups
    print('Произошла ошибка при выполнении запроса:', response.status_code)


def get_groups_by_query(query: str) -> list[Any] | None:
    """Возвращает список групп по запросу."""
    URL = 'https://api.vk.com/method/groups.search'
    params = {
        'access_token': ACCESS_TOKEN,
        'v': VK_API_VERSION,
        'count': 500,
        'q': query,
    }
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        results = response.json().get('response', {}).get('items', [])
        return results
    print('Произошла ошибка при выполнении запроса:', response.status_code)


def groups_id(data: list[int]) -> list[int]:
    """Возвращает ID групп, принимает список групп."""
    groups_id: list[int] = [group_id.get('id') for group_id in data]
    return groups_id


def get_groups_user_by_query(user_id: int, query: str)  -> list | None:
    """Возвращает список ID групп, найденных по запросу и у юзера"""
    groups: list[Any] | None = get_groups_by_query(query)
    search_groups: list[int] = groups_id(groups)
    user_groups: list[int] | None = get_id_user_groups(user_id)
    results = set(search_groups).intersection(set(user_groups))
    return list(results)


def get_user_friends(user_id: int) -> list | None:
    """Возвращает список друзей юзера."""
    URL = 'https://api.vk.com/method/friends.get'
    params = {
        'access_token': ACCESS_TOKEN,
        'v': VK_API_VERSION,
        'user_id': user_id,
    }
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        return response.json().get('response', {}).get('items', [])
    print('Произошла ошибка при выполнении запроса:', response.status_code)


def get_user_groups_with_friends(user_id: int) -> list | None:
    """Возвращает список ID групп юзера и его друзей."""
    all_groups_id = set()
    user_groups_id: list[int] | None = get_id_user_groups(user_id)
    all_groups_id = all_groups_id.union(user_groups_id)
    friends_id: list[int]  | None = get_user_friends(user_id)
    for friend_id in friends_id:
        groups_id: list[int] | None = get_id_user_groups(friend_id)
        all_groups_id = all_groups_id.union(groups_id)
    return list(all_groups_id)


def search_group_with_friends(user_id: int, query: str) -> list[int] | None:
    """Поиск групп по подстроке, в которые входит юзер и его друзья."""
    groups: list[Any] | None = get_groups_by_query(query)
    search_groups: list[int] = groups_id(groups)
    user_and_friends_groups_id: list[int] | None = (
        get_user_groups_with_friends(user_id)
    )
    results_id = (
        set(search_groups).intersection(set(user_and_friends_groups_id))
    )
    results = []
    for group in groups:
        if group.get('id') in results_id:
            results.append(
                dict(
                    group_id = group.get('id'),
                    group_name = group.get('name'),
                )
            )
    return results
