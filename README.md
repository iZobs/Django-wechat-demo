##1.ln mysite.conf and restart nginx

```
sudo ln -s /root/workspace/izobs/hello/mysite.conf /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart

```
##2.star server thought uswgi

```
uwsgi --ini ./mysite_uwsgi.ini

```
##3.django logger
watch the django_all.log to see what happen in django

> logger.info('it is get')

```
tail -f ./django_all.log
```

