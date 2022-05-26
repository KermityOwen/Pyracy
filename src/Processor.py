import pytube
from pytube.cli import on_progress
import os, sys

'''
def progress_function(stream, chunk, file_handle, bytes_remaining):
    filesize = stream.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()
'''

def map_choices(urllist):
    """
    Remaps urls into yt objects readable and usable by the pytube api

    Args:
        urllist: list of urls of videos to map from

    Return:
        list of pytube.YouTube objects mapped from urllist
    """
    yt_list = []
    list(map(lambda og_url: yt_list.append(pytube.YouTube(og_url, on_progress_callback=on_progress)), urllist))
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
        ytlist: list of pytube.YouTube objects
        choice: choice of the video to specify

    Returns:
        A pytube stream object from the highest resolution of the yt object specified

    """
    yt_obj = ytlist[choice]
    stream = yt_obj.streams.get_highest_resolution()
    return stream

