DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #사용엔진 -mysql
        'NAME': 'skku_schedule', #데이터베이스(스키마) 이름
        'USER' : 'root', # DB접속 계정명
        'PASSWORD' : 'hamyfa88jh@', #DB비밀번호
        'HOST' :'localhost', # 실제 DB주소
        'PORT' : '3306', # DB포트번호
    }
}

SECRET_KEY = 'django-insecure-0f9cv)y#19q8%-6!&h#pyz2c&nyk3p0e$e_ok!1da=f%22kom-'