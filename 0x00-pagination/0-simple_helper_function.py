#!/usr/bin/env python3
def index_range(page, page_size):
    """ create index_range """
    p = page - 1
    start = p * page_size
    end = page * page_size
    return start, end
