# mtls_grpc_sample

Login with "sijunliu@contextaware.us".
```
gcloud auth login
gcloud config set project sijun-mtls-demo
```

Download the repo:
```
git clone https://github.com/arithmetic1728/mtls_grpc_sample.git
```

Create a virtual environment:
```
pyenv virtualenv mtls_grpc_sample
pyenv local mtls_grpc_sample
```

Install the following in order.
```
python -m pip install -e pubsub
```

Run the sample, `python grpc_sample.py`

This repo also contains a http sample. To run it:
```
python -m pip install pyopenssl
python http_sample.py
```
