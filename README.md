# File Manager

### Prerrequisitos

- Python 3.8.10

### Dependencias
```
asgiref==3.7.2
backports.zoneinfo==0.2.1
certifi==2023.11.17
charset-normalizer==3.3.2
Django==4.2.7
djangorestframework==3.14.0
httplib2==0.22.0
idna==3.6
pyasn1==0.5.1
pycparser==2.21
pyparsing==3.1.1
pytz==2023.3.post1
requests==2.31.0
rsa==4.9
sqlparse==0.4.4
typing-extensions==4.8.0
tzdata==2023.3
uritemplate==4.1.1
urllib3==2.1.0

```

### Instalar las dependencias

```
python -m pip install -r requirements.txt
```

### Iniciar base de datos

```
python manage.py migrate
```

### Correr el servidor
```
python manage.py runserver
```