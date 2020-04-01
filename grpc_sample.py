import google.oauth2.credentials
from google.pubsub import PublisherClient
import google.api_core.client_options as ClientOptions


def call():
    _, project_id = google.auth.default()

    print("=========== project id ====")
    print(project_id)

    cred = google.oauth2.credentials.UserAccessTokenCredentials()
    client_options = ClientOptions.ClientOptions(
        api_endpoint="pubsub.mtls.googleapis.com"
    )
    client = PublisherClient(credentials=cred, client_options=client_options)

    project = "projects/{}".format(project_id)
    list_topics_iter = client.list_topics(project=project)

    topics = list(list_topics_iter)
    print(topics)


call()
