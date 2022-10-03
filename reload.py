import os

os.system("sudo systemctl restart gunicorn")
os.system("sudo systemctl daemon-reload")
os.system("sudo systemctl restart gunicorn.socket gunicorn.service")
os.system("sudo nginx -t && sudo systemctl restart nginx")
print('server reloaded')

#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
