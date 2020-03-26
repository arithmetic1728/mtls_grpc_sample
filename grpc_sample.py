import google.oauth2.credentials
from google.pubsub import PublisherClient
import google.api_core.client_options as ClientOptions


def call():
    _, project_id = google.auth.default()

    print("=========== project id ====")
    print(project_id)

    cred = google.oauth2.credentials.UserAccessTokenCredentials() 
    client = PublisherClient(
        credentials=cred, api_mtls_endpoint="pubsub.mtls.googleapis.com"
    )

    project = "projects/{}".format(project_id)
    list_topics_iter = client.list_topics(project=project)

    topics = list(list_topics_iter)
    print(topics)


call()
