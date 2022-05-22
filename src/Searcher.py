import requests
import os
import re


def search_for_title_http(title: str) -> str:
    """
    Search for the first found video with the title from youtube and return the html source for that page.

    Args:
        title: Search terms of the page used to search for the video

    Returns:
        HTML source for the page searched
    """
    f = re.compile(r" ")
    title = re.sub(f, "+", title)
    url = "https://www.youtube.com/results?search_query=" + title
    source = requests.get(url)
    return source.content.decode("utf-8")


def filter_video_links(source: str, n=50):
    """
    Searches and filters the page links for the videos

    Args:
        source: HTML Source to be filtered
        n: Size of arraylist to be returned (default: n=50)

    Returns:
        A list of strings of filtered urls
    """
    f = re.compile(r'/watch\?v=.*?"')
    temp_list = re.findall(f, source)
    temp_list = list(map(lambda og_string: og_string.replace('/', 'youtube.com/'), temp_list))
    # Lambda for temporary function that returns the argument it takes after removing all " and replacing the front
    # of the string with "youtube.com"
    # Map provides the argument by iterating through the lists strings and the above lambda function to each element
    url_list = list(map(lambda og_string: og_string.replace('"', ''), temp_list))
    return list_slicer(url_list, n)


def list_slicer(url_list, size):
    """
    Slices the list into a certain size

    Args:
        url_list: List of urls
        size: Size of list to be cut down to

    Returns:
        New list of size "size"
    """
    return url_list[0:size]


if __name__ == "__main__":
    html_source = search_for_title_http("reverb fart")
    urls = filter_video_links(html_source)
    print(urls)

