from flask import url_for

from app.constants import SUCCESS, CALL_NOT_NULL, PARM_FORMAT_ERROR, EMAIL_FORMAT_ERROR


def test_group_all(client):
    res = client.get(url_for('index.all_group_details'))
    assert res.json['status'] == SUCCESS


def test_group_create(client):
    # correct data
    data = {
        'name': '老尹',
        'college': 0,
        'grade': 0,
        'qq': '123456',
        'email': '123@qq.com',
    }
    res = client.post(url_for('index.group_participate'), data=data)
    assert res.json['status'] == SUCCESS

    group_id = res.json['data']['group_id']
    res = client.get(url_for('index.group_details', group_id=group_id))
    assert res.json['status'] == SUCCESS

    for field in data:
        assert data[field] == res.json['data'][field]

    # 联系情况为空
    data = {
        'name': '老尹',
        'college': 0,
        'grade': 0,
    }
    res = client.post(url_for('index.group_participate'), data=data)
    assert res.json['status'] == CALL_NOT_NULL

    # college 选择值不对
    data = {
        'name': '老尹',
        'college': 3,
        'grade': 0,
        'qq': '123'
    }
    res = client.post(url_for('index.group_participate'), data=data)
    assert res.json['status'] == PARM_FORMAT_ERROR

    # email 格式错误
    data = {
        'name': '老尹',
        'college': 3,
        'grade': 0,
        'email': '123'
    }
    res = client.post(url_for('index.group_participate'), data=data)
    assert res.json['status'] == EMAIL_FORMAT_ERROR
