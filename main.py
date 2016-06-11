import threading
from queue import Queue

from spider import Spider

PROJECT_NAME = 'pilka_nozna'
PAGE = 'http://www.tablesleague.com/livescores/'
NUMBER_OF_THREADS = 1
Spider(PAGE)


# Tworzenie wątków zadań
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Wykonywanie kolejnych zadań
def work():
    Spider.crawl_page(threading.current_thread().name, PAGE)

create_workers()
