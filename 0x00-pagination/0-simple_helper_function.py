#!/usr/bin/env python3
""" 0-0-simple_helper_function"""
def index_range(page, page_size: int):
    """ create index_range """
    page_index = (page - 1) * page_size, page * page_size
    return page_index
