import google.auth
from google.pubsub import PublisherClient


def call():
    credentials, project_id = google.auth.default()

    print("=========== project id ====")
    print(project_id)
    print("=========== credentials ====")
    print(credentials)

    credentials = google.auth.credentials.with_scopes_if_required(
        credentials, ["https://www.googleapis.com/auth/pubsub"]
    )

    client = PublisherClient(credentials=credentials)

    project = "projects/{}".format(project_id)
    list_topics_iter = client.list_topics(project=project)

    topics = list(list_topics_iter)
    print(topics)


call()
