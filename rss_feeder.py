"""
Purpose: File to create a RSS feed reader in Python
Date Created: 1st November 2024
Author: Harmandeep Kaur Kaler
"""

import feedparser
import html2text

class RSSfeedReader(object):
    """
        Class to act as a feed reader
    """
    def __init__(self) -> None:
        pass

    @staticmethod
    def feed_reader(url):
        """
            Input: URL
            Output: Parsed Feed
        """
        try:
            response_article = []
            parsed_feed = feedparser.parse(url)
            for article in parsed_feed["entries"]:
                response_article.append({
                    "Title": article["title"],
                    "Description": html2text.html2text(article["summary"]),
                    "Author": article["author"],
                    "Date Published": article["published"],
                    "Last Updated": article["updated"]
                })
            return response_article
        except Exception as ex:
            return "An error occurred while getting the content from Medium" + str(ex)

# ask for the input url
url = input("Please input the medium URL you want the RSS feed for: ")
feed_response = RSSfeedReader.feed_reader(url)
print("The RSS feed for the input URL:\n", feed_response)
