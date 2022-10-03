import os

print('*********************************GUNICORN STATUS***********************************')
os.system("sudo systemctl status gunicorn")
print('*********************************GUNICORN STATUS***********************************')

print('*********************************NGINX SERVER STATUS***********************************')
os.system("sudo systemctl status nginx")
print('*********************************NGINX SERVER STATUS***********************************')

print('*********************************POSTGRESQL DATABASE SERVER STATUS***********************************')
os.system("sudo systemctl status postgresql")
print('*********************************POSTGRESQL DATABASE SERVER STATUS***********************************')

#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
