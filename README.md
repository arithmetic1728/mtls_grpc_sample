# mtls_grpc_sample

```
gcloud auth application-default login --scopes="https://www.googleapis.com/auth/pubsub"
gcloud config set project sijun-mtls-demo
```

Download the repo:
```
git clone --recursive https://github.com/arithmetic1728/mtls_grpc_sample.git
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

Run the sample, `python grpc_sample.py`

This repo also contains a http sample. To run it:
```
python -m pip install pyopenssl
python http_sample.py
```
