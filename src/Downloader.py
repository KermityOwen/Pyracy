import os


def download_video(ys, path):
    """
    Downloads video from pytube stream

    Args:
        ys: the stream object to download from
        path: path to download to

    Returns:
        None
    """
    if path is None:
        path = f"{os.getenv('USERPROFILE')}\\Downloads"
    try:
        ys.download(path)
    except FileNotFoundError:
        print("Path not found. Redirecting download to %s" % path)
