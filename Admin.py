from Client import Client
import re


def verification_of_login(client):
    if re.match(r'^[a-zA-Z0-9]+$', client.login):
        return True
    return False


def verification_of_signing_in(client):
    if re.match(r'^[a-zA-Z]+$', client.name and client.surname):
        return True
    return True
