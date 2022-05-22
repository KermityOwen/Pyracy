import requests
import os
import re
import pytube
import Searcher


def map_choices(urllist):
    """
    Remaps urls into yt objects readable and usable by the pytube api

    Args:
        urllist: list of urls of videos to map from

    Return:
        list of pytube.YouTube objects mapped from urllist
    """
    yt_list = []
    list(map(lambda og_url: yt_list.append(pytube.YouTube(og_url)), urllist))
    return yt_list


def display_titles(ytlist):
    """
    Display all titles from ytlist

    Args:
        ytlist: list of pytube.YouTube objects
    """
    i = 1
    for x in ytlist:
        try:
            print("%s." % str(i) + x.title)
        except:
            print("%s.!!!ERROR VIDEO TITLE CANNOT BE PROCESSED!!!" % str(i))
        i = i + 1


def specify_video(ytlist, choice=0):
    """
    Specifies a singular yt object from the list of yts

    Args:
        ytlist:
        choice:

    Returns:

    """
    yt_obj = ytlist[choice]
    stream = yt_obj.streams.get_highest_resolution()
    return stream


def download_video(ys, path=None):
    ys.download(path)


if __name__ == "__main__":
    htmlsrc = Searcher.search_for_title_http(str(input("Search: ")))
    urls = Searcher.filter_video_links(htmlsrc, 10)
    yts = map_choices(urls)
    display_titles(yts)
    ystream = specify_video(yts, int(input("Choice: "))-1)
    download_video(ystream, f"{os.getenv('USERPROFILE')}\\Downloads")
