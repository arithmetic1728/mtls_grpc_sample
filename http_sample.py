import json
from os import path

import google.auth
import google.auth.credentials
import google.auth.transport.requests
import google.auth.transport.urllib3

MTLS_ENDPOINT = "https://pubsub.mtls.googleapis.com/v1/projects/{}/topics"
REGULAR_ENDPOINT = "https://pubsub.googleapis.com/v1/projects/{}/topics"

credentials, project_id = google.auth.default()
credentials = google.auth.credentials.with_scopes_if_required(
    credentials, ["https://www.googleapis.com/auth/pubsub"]
)
print("======= project_id ========")
print(project_id)
print("======= credentials ========")
print(credentials)


def use_requests():
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)
    authed_session.configure_mtls_channel()

    if authed_session.is_mtls:
        print("====== use mtls channel=====")
        response = authed_session.get(MTLS_ENDPOINT.format(project_id))
    else:
        print("====== use regular channel=====")
        response = authed_session.get(REGULAR_ENDPOINT.format(project_id))

    print(response.content)


def use_urllib3():
    authed_http = google.auth.transport.urllib3.AuthorizedHttp(credentials)
    is_mtls = authed_http.configure_mtls_channel()

    if is_mtls:
        print("====== use mtls channel=====")
        response = authed_http.request("GET", MTLS_ENDPOINT.format(project_id))
    else:
        print("====== use regular channel=====")
        response = authed_http.request("GET", REGULAR_ENDPOINT.format(project_id))

    print(response.data)


use_requests()
use_urllib3()
