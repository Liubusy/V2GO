### Django forum SAE

***

demo: <http://v2go.sinaapp.com/>

#### ��װ����

������:

����MySQL���ݿ�,�Լ�memcached

1. ��ȡ����
2. ��װ����
3. �������ݿ��ļ�
4. �޸������ļ�
5. ���з���

```shell
shell> cd forum
shell> pip install -r requirements.txt

shell> mysql -u YOURUSERNAME -p

mysql> create database forum;
mysql> exit

shell> mysql -u YOURUSERNAME -p --database=forum < forum.sql
```

�޸�`xp/settings.py`

```python
# �޸����ݿ�����
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'forum',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}
```
# �޸�memcached����,���û��memcahed��ɾ����Щ��cache��ص�����
CACHES = { # memcached��������
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache' # ʹ��memcached�洢session

# �����ʼ�����
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER= '*********'
EMAIL_HOST_PASSWORD= '******'
DEFAULT_FROM_EMAIL = '*********@qq.com'
```

���з���

```shell
python manage.py runserver
```

Ĭ�ϳ����û�`admin@forum.com`,����`123456`,��̨`/manage/admin/`

python
# �ʼ���������
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER= '*********'
EMAIL_HOST_PASSWORD= '******'
DEFAULT_FROM_EMAIL = '*********@qq.com'
