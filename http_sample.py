import json
from os import path

import google.auth
import google.auth.credentials
import google.auth.transport.requests
import google.auth.transport.urllib3
from google.oauth2 import credentials

MTLS_ENDPOINT = "https://pubsub.mtls.googleapis.com/v1/projects/{}/topics"
REGULAR_ENDPOINT = "https://pubsub.googleapis.com/v1/projects/{}/topics"

_, project_id = google.auth.default()
credentials = credentials.UserAccessTokenCredentials()
print("project_id is: ")
print(project_id)


def use_requests():
    print("\n\n====== Test http call with requests lib =====\n")
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)
    authed_session.configure_mtls_channel()

    if authed_session.is_mtls:
        print("= using mtls channel=")
        response = authed_session.get(MTLS_ENDPOINT.format(project_id))
    else:
        print("= using regular channel=")
        response = authed_session.get(REGULAR_ENDPOINT.format(project_id))

    print(response.content)


def use_urllib3():
    print("\n\n====== Test http call with urllib3 lib =====\n")
    authed_http = google.auth.transport.urllib3.AuthorizedHttp(credentials)
    is_mtls = authed_http.configure_mtls_channel()

    if is_mtls:
        print("= using mtls channel=")
        response = authed_http.request("GET", MTLS_ENDPOINT.format(project_id))
    else:
        print("= using regular channel=")
        response = authed_http.request("GET", REGULAR_ENDPOINT.format(project_id))

    print(response.data)


use_requests()
use_urllib3()
