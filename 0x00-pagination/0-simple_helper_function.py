#!/usr/bin/env python3
def index_range(page: int, page_size: int) -> tuple:
    """ create index_range """
    return (page - 1) * page_size, page * page_size
