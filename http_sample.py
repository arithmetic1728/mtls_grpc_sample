import json
from os import path

import google.auth
import google.auth.credentials
from google.auth.transport import mtls
import google.auth.transport.requests
import google.auth.transport.urllib3
from google.oauth2 import credentials

MTLS_ENDPOINT = "https://pubsub.mtls.googleapis.com/v1/projects/{}/topics"
REGULAR_ENDPOINT = "https://pubsub.googleapis.com/v1/projects/{}/topics"
project_id = "sijun-mtls-demo"
credentials = credentials.UserAccessTokenCredentials()


def use_requests():
    print("\n\n====== Test http call with requests lib =====\n")
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)

    if mtls.has_default_client_cert_source():
        print("= has default client cert source=")
        callback = mtls.default_client_cert_source()
    else:
        callback = None

    authed_session.configure_mtls_channel(client_cert_callback=callback)

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

    if mtls.has_default_client_cert_source():
        print("= has default client cert source=")
        callback = mtls.default_client_cert_source()
    else:
        callback = None

    is_mtls = authed_http.configure_mtls_channel(client_cert_callback=callback)

    if is_mtls:
        print("= using mtls channel=")
        response = authed_http.request("GET", MTLS_ENDPOINT.format(project_id))
    else:
        print("= using regular channel=")
        response = authed_http.request("GET", REGULAR_ENDPOINT.format(project_id))

    print(response.data)


use_requests()
use_urllib3()
