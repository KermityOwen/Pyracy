import Searcher
import Processor
import Downloader
import json
import os

""" ~~~ MAIN ~~~ """
config_path = os.path.abspath("../config.json")

with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

search_url = Searcher.compile_search_url(str(input("Search: ")))
print("---")
htmlsrc = Searcher.get_html_as_string(search_url)
urls = Searcher.filter_video_links(htmlsrc, 10)
yts = Processor.map_choices(urls)
Processor.display_titles(yts)
print("---")
ystream = Processor.specify_video(yts, int(input("Choice: ")) - 1)
print("---")
Downloader.download_video(ystream, config["dl_path"])

input("\nDownloaded. Press ENTER to end program.")
