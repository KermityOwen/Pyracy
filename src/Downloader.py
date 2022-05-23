import os
import Processor
import Searcher


def download_video(ys, path=None):
    """
    Downloads video from pytube stream

    Args:
        ys: the stream object to download from
        path: path to download to

    Returns:
        None
    """
    ys.download(path)


if __name__ == "__main__":
    search_url = Searcher.compile_search_url(str(input("Search: ")))
    htmlsrc = Searcher.get_html_as_string(search_url)
    urls = Searcher.filter_video_links(htmlsrc, 10)
    yts = Processor.map_choices(urls)
    Processor.display_titles(yts)
    ystream = Processor.specify_video(yts, int(input("Choice: "))-1)
    download_video(ystream, f"{os.getenv('USERPROFILE')}\\Downloads")
