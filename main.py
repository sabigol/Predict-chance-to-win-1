#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading

from spider import Spider

PAGE = 'http://www.tablesleague.com/livescores/'
Spider(PAGE)


# Tworzenie wątków zadań
def create_workers():
    work()


# Wykonywanie kolejnych zadań
def work():
    Spider.crawl_page(threading.current_thread().name, PAGE)

create_workers()


# 1. Program pobiera dane na temat meczy piłkarskich i % szans na wynik meczu ze strony: (za pomocą klasy spider)
# 2. W main można podać liczbę wątków na których można to włączyć, ale nie ma potrzeby, gdy jest 1 link
# 3. dostepnej w zmiennej PAGE = 'http://www.tablesleague.com/livescores/'
# 4. Parsuje pobrane wyniki za pomocą biblioteki Beautyfull soup
# 5. Następnie zapisuje je w bazie danych MySQL (dane do uzupełnienia w obiektach klasy MySQLConnector)
