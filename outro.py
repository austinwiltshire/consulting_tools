#!/usr/bin/env python3

from collections import namedtuple
from urllib.parse import urlencode, urlunparse, quote

TWITTER_LINK = "https://twitter.com/GuildmasterC"
PODCAST_LINK = "https://www.youtube.com/results?search_query=guildmaster+consulting"
LINKEDIN_LINK = "https://www.linkedin.com/company/guildmaster-consulting"

# namedtuple to match the internal signature of urlunparse
Components = namedtuple(typename="Components", field_names=["scheme", "netloc", "path", "params", "query", "fragment"])


def make_reddit_link(title: str, blog_url: str) -> str:
    """
    Generates a link that will share a blog with title to reddit

    :param title: The title of the blog
    :param blog_url: The url to the wix blog
    :return: A string with the url that will share the title of the blog to reddit
    """

    return urlunparse(
        Components(
            scheme="https",
            netloc="www.reddit.com",
            path=f"/submit",
            params="",
            query=urlencode({"url": blog_url, "title": title}, quote_via=quote),  # reddit uses old quoting
            fragment="",
        )
    )


def make_hacker_news_link(title: str, blog_url: str) -> str:
    """
    Generates a link that will share a blog with title to hacker news

    :param title: The title of the blog
    :param blog_url: The url to the wix blog
    :return: A string with the url that will share the title of the blog to hacker news
    """

    return urlunparse(
        Components(
            scheme="https",
            netloc="news.ycombinator.com",
            path=f"/submitlink",
            params="",  # {"u": blog_url},
            query=urlencode({"u": blog_url, "t": title}, quote_via=quote),
            fragment="",
        )
    )


def make_wix_title(title: str) -> str:
    """
    Turns a title in english into a lowercase-dash-delimited-no-other-punctuation encoding

    A wix title is used in the wix blog's url

    www.wix.com/posts/wix-title-goes-here -> points to a blog titled "Wix Title: Goes here"

    :param title: The title in the King's English
    :return: a-dash-delimited-string
    """

    wix_drop_list = ":,?!."

    # Drop bad chars, replace spaces with dashes, replace apostrophes with dashes, and lowercase it.
    return drop_chars(title, wix_drop_list).replace(" ", "-").replace("'", "-").lower()


def drop_chars(drop_from: str, char_list: str) -> str:
    """
    Drops all instances of characters in char_list from drop_from

    :param drop_from: A string that the char_list characters will be removed from
    :param char_list: The list of characters to remove from drop_from
    :return: A new string based on drop_from except with each individual character from char_list removed
    """

    # We use translate to do this, but it expects the ordinal unicode number to work. We replace each character with
    # none, which drops the character
    return drop_from.translate({ord(i): None for i in char_list})


def make_wix_link(title: str) -> str:
    """
    Generate the url of the blog with a certain title on Guildmaster's blog site

    :param title:  The title of the blog
    :return: The url as a string
    """

    title = make_wix_title(title)

    url = urlunparse(
        Components(
            scheme="https",
            netloc="www.guildmasterconsulting.com",
            path=f"/post/{title}",
            params="",
            query=urlencode({}),
            fragment="",
        )
    )

    return url


def outro_generator(title: str) -> str:
    """
    Takes in the title of the blog and generates the outro in markdown.

    Contains links to share and follow us, as well as standard messaging.

    :param title:  Blog's title without any formatting, space separated
    :return: The full outro ready to be printed to screen and copy pasted.
    """

    blog_url = make_wix_link(title)

    messaging = f"""**We're on a mission to make jobs suck less, one software management tip at a time. We need your help!**

- [Share to Reddit]({make_reddit_link(title, blog_url)})
- [Share to Hacker News]({make_hacker_news_link(title, blog_url)})

Do you want to stay up to date on the latest management tips to help your team stay productive?

Click "Subscribe to the Soapbox" below for more!

- [Follow us on Twitter]({TWITTER_LINK})
- [Subscribe to our Podcast]({PODCAST_LINK})
- [Follow us on LinkedIn]({LINKEDIN_LINK})"""

    return messaging


if __name__ == "__main__":
    import sys

    if not sys.argv[1]:
        print('Usage: python3 outro.py "This is the title I want to use"')

    print(outro_generator(sys.argv[1]))
