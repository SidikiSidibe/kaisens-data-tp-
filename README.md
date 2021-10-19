# Api détection toxicité des posts twitter

# company : KAISENS DATA

## V1.0

## Requirements
* Api toxicity detection installer on your local machine

* python >= 3.7

##  Dev

create a virtual env : 
```
pip install virtualenv
```

virtualenv ENVIRONMENT_NAME

On windows you can activate it with the following command : . ENVIRONMENT_NAME\Scripts\activate.bat

```

all mdoules require installation
```
pip install -r requirements.txt
pip freeze > requirements.txt 

```

lauch app
```
python app.py
```

build image docker
```
docker build -t api-toxicity:latest .
```

run the container
```
docker run -d -p 5000:5000 api-toxicity
```
