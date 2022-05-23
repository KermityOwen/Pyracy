import Searcher
import Processor
import Downloader
import json
import os

if __name__ == "__main__":
    # ~~~ MAIN ~~~ #
    base_path = os.path.dirname(__file__)
    config_path = os.path.join(base_path, "..", "config.json")

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    search_url = Searcher.compile_search_url(str(input("Search: ")))
    htmlsrc = Searcher.get_html_as_string(search_url)
    urls = Searcher.filter_video_links(htmlsrc, 10)
    yts = Processor.map_choices(urls)
    Processor.display_titles(yts)
    ystream = Processor.specify_video(yts, int(input("Choice: ")) - 1)
    Downloader.download_video(ystream, config["dl_path"])
