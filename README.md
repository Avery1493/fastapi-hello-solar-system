```pip install pipx```  
```pipx ensurepath```  
```pipx install awsebcli```  
```eb --help```


```pip install pipenv```  
```pipenv install fastapi uvicorn gunicorn```  
```pipenv shell```  
```pipenv install pandas```  
```pipenv install tabulate```      

```uvicorn main:app --reload```


Procfile ```web: gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker```

Deploy to Elastic Beanstalk  
```eb init --platform python-3.7 make-up-your-app-name --region us-east-1```  
```eb create make-up-your-environment-name```   
```eb open```


