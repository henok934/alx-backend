#!/usr/bin/env python3
def index_range(page, page_size: int):
    """ create index_range """
    return (page - 1) * page_size, page * page_size
