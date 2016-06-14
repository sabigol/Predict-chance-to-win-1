#!/usr/bin/env python
# -*- coding: utf-8 -*-
from match_finder import MatchFinder


class Spider:

    base_url = ''

    def __init__(self, base_url):
        Spider.base_url = base_url
        self.crawl_page('Spider', Spider.base_url)

    @staticmethod
    def crawl_page(thread_name, page_url):
        print(thread_name + ' crawling ' + page_url)
        finder = MatchFinder(page_url)
        finder.fetch_matchs()
