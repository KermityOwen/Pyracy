import urllib
import re


def compile_search_url(searchterm: str):
    """
    Compiles YouTube's url with the search term of argument

    Args:
        searchterm: search term to be added url

    Returns:
        url of the YouTube page when searchterm is searched
    """
    f = re.compile(r" ")
    f_searchterm = re.sub(f, "+", searchterm)
    url = "https://www.youtube.com/results?search_query=" + f_searchterm
    return url


def get_html_as_string(url: str) -> str:
    """
    Returns the html source for the url given

    Args:
        url: the url we are getting the html source from

    Returns:
        HTML source for url
    """
    request = urllib.request.urlopen(url)
    source_byte = request.read()
    return source_byte.decode("utf-8")


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
