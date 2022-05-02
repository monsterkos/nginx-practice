# import multiprocessing

bind = "0.0.0.0:8080"
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 3
worker_class = "common_lib.uvicorn_worker.RestartableUvicornWorker"
# worker_class = "uvicorn.workers.UvicornWorker"
wsgi_app = "nginx_practice.main:app"
reload = True
