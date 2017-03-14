from app.constants import status_message


def response_dict(status, message=None, data=None):
    if message is None:
        message = status_message[status]

    if data is None:
        data = {}

    return {'status': status, 'message': message, 'data': data}
