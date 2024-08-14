#!/usr/bin/env python3
"""Module for caching web page content using Redis."""

import requests
import redis
from functools import wraps
import time


redis_client = redis.Redis()


def cache_with_expiration(expiration_time):
    """Decorator for caching function results with expiration."""
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            cache_key = f"cache:{url}"
            cached_result = redis_client.get(cache_key)
            if cached_result:
                return cached_result.decode('utf-8')
            result = func(url)
            redis_client.setex(cache_key, expiration_time, result)
            return result
        return wrapper
    return decorator


def count_access(func):
    """Decorator for counting URL accesses."""
    @wraps(func)
    def wrapper(url):
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return func(url)
    return wrapper


@count_access
@cache_with_expiration(10)
def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = (
        "http://slowwly.robertomurray.co.uk/delay/1000/url/"
        "http://www.example.com"
    )

    start = time.time()
    content = get_page(url)
    print(f"Time taken: {time.time() - start:.2f} seconds")

    start = time.time()
    content = get_page(url)
    print(f"Time taken: {time.time() - start:.2f} seconds")

    count = redis_client.get(f"count:{url}")
    print(f"URL accessed {count.decode('utf-8')} times")

    print("Waiting for cache to expire...")
    time.sleep(11)

    start = time.time()
    content = get_page(url)
    print(f"Time taken: {time.time() - start:.2f} seconds")

    count = redis_client.get(f"count:{url}")
    print(f"URL accessed {count.decode('utf-8')} times")
