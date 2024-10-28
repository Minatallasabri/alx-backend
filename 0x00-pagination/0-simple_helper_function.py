#!/usr/bin/env python3
"""
Main file
"""


def index_range(page: int, page_size: int) -> tuple:
    """_summary_

    Args:
        page (int): _description_
        page_size (int): _description_

    Returns:
        tuple: _description_
    """
    return (page*page_size-page_size, page_size*page)
