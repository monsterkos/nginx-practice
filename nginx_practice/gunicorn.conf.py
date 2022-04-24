# import multiprocessing

bind = "0.0.0.0:80"
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
wsgi_app = "nginx_practice.main:app"
reload = True
