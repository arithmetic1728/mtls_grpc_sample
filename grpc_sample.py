from google.auth.transport import mtls
import google.oauth2.credentials
from google.pubsub import PublisherClient
import google.api_core.client_options as ClientOptions


def call():
    project_id = "sijun-mtls-demo"

    cred = google.oauth2.credentials.UserAccessTokenCredentials()

    if mtls.has_default_client_cert_source():
        print("= has default client cert source=")
        callback = mtls.default_client_cert_source()
    else:
        callback = None

    client_options = ClientOptions.ClientOptions(
        api_endpoint="pubsub.mtls.googleapis.com", client_cert_source=callback
    )
    client = PublisherClient(credentials=cred, client_options=client_options)

    project = "projects/{}".format(project_id)
    list_topics_iter = client.list_topics(project=project)

    topics = list(list_topics_iter)
    print(topics)


call()
