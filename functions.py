import requests


def get_token_password(cr_url, username, password):
    endpoint = "/v1/authentication"
    url = cr_url + endpoint
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "username": username,
        "password": password
    }

    r = requests.post(url=url, headers=headers, json=payload, verify=False)
    r.raise_for_status()
    return r.json()['token']


def get_token_apikey(cr_url, username, api_key):
    endpoint = "/v1/authentication"
    url = cr_url + endpoint
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "username": username,
        "apiKey": api_key
    }

    r = requests.post(url=url, headers=headers, json=payload, verify=False)
    r.raise_for_status()
    return r.json()['token']


def get_credential_list(cr_url, token):
    endpoint = "/v2/credentialvault/credentials/list"
    url = cr_url + endpoint
    headers = {
        "Content-Type": "application/json",
        "X-Authorization": token
    }

    payload = {
        "filter": {

        }
    }

    r = requests.post(url=url, headers=headers, json=payload, verify=False)
    r.raise_for_status()
    return r.json()['list']


def get_attribute_values(cr_url, token, credential_id, credential_attribute_id):
    endpoint = f"/v2/credentialvault/credentials/{credential_id}/attributevalues?credentialAttributeId={credential_attribute_id}"
    url = cr_url + endpoint
    headers = {
        "Content-Type": "application/json",
        "X-Authorization": token
    }
    # print(url)
    r = requests.get(url=url, headers=headers, verify=False)
    r.raise_for_status()
    return r.json()['list']
