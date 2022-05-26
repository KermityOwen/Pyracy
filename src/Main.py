import Searcher
import Processor
import Downloader
import json
import os, sys


""" ~~~ MAIN ~~~ """
config_path = os.path.abspath("./config.json")

with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)


def main():
    search_url = Searcher.compile_search_url(str(input("Search: ")))
    print("---")

    htmlsrc = Searcher.get_html_as_string(search_url)
    urls = Searcher.filter_video_links(htmlsrc, 10)
    yts = Processor.map_choices(urls)
    Processor.display_titles(yts)
    print("---")

    choice = int(input("Choice: ")) - 1
    ystream = Processor.specify_video(yts, choice)
    print("---")

    Downloader.download_video(ystream, config["dl_path"])
    print("---")

    exitstr = input("\nDownloaded. Exit program? (Y/N): ")

    if exitstr == "n" or exitstr == "N":
        os.system("cls")
        main()


main()
