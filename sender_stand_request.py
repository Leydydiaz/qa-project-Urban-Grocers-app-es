def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=configuration.headers)

def get_kit_body(name):
    kit_body = {
        "name": name
    }
    return kit_body

def post_new_kit(kit_body, auth_token):
    headers = configuration.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)
