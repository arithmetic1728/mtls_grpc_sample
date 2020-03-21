# mtls_grpc_sample

```
gcloud auth application-default login --scopes="https://www.googleapis.com/auth/pubsub"
gcloud config set project sijun-mtls-demo
```

Create a virtual environment:
```
pyenv virtualenv mtls_grpc_sample
pyenv local mtls_grpc_sample
```

Then go to `google-auth-library-python` and `pubsub` directories, install them
locally with command
```
python -m pip install -e .
```

Run the sample, `python sample.py`
