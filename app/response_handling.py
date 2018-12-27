"""Module created to handle standard API responses."""

from flask import jsonify
from status_codes import error, success


def user_created():
    return response(success['Created'])


def success_login(tokens):
    return response(success['Authorized'], tokens)


def success_list_users(user_list):
    return jsonify({
        'code': success['Admin_Authorized'][0],
        'message': success['Admin_Authorized'][1],
        'user_list': user_list
    })


def wrong_login_details():
    return response(error['Unauthorized'])


def pw_change_success():
    return response(success['Password_Changed'])


def unknown_user():
    return response(error['Unknown_User'])


def existing_user():
    return response(error['Existing_User'])


def user_deleted(user_to_delete):
    return response(success['User_Deleted'], user_to_delete)


def internal_error(message):
    return response(error['Internal_Error'], message)


def string_compare_ratio_result(original, new, ratio):
    return jsonify({
        'code': 202,
        'message': 'Login accepted and successfully compared text.',
        'original': original,
        'new text': new,
        'ration': ratio
    })


def urls_not_valid():
    return response(error['Urls'])


def response(code, special=''):
    print('Preparing response with {}!'.format(str(code[0])))
    return jsonify({
        'code': code[0],
        'message': code[1] + special
    })
