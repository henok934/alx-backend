#!/usr/bin/env python3
def index_range(page: int, page_size: int) -> tuple:
    """ create index_range """
    page_index = (page - 1) * page_size, page * page_size
    return page_index
