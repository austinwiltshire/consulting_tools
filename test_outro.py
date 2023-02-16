"""
Tests for the outro file
"""

import outro

TITLE = "Organizing Confluence Pages: How to Conquer Your Mess With Tags"


def test_drop_chars():
    """Tests that drop chars on a string removes the characters"""
    assert outro.drop_chars("ABCabc456DEFdef123", "1aD") == "ABCbc456EFdef23"


def test_wix_title():
    """Tests that a wix title properly changes the english title to a wix-one"""
    assert (
        outro.make_wix_title("Organizing Confluence Pages: How to Conquer Your Mess With Tags")
        == "organizing-confluence-pages-how-to-conquer-your-mess-with-tags"
    )


def test_make_wix_link():
    wix_link = outro.make_wix_link(title=TITLE)

    assert (
        wix_link
        == "https://www.guildmasterconsulting.com/post/organizing-confluence-pages-how-to-conquer-your-mess-with-tags"
    )


def test_make_reddit_link():
    title = "Organizing Confluence Pages: How to Conquer Your Mess With Tags"
    wix_link = outro.make_wix_link(title)

    assert (
        outro.make_reddit_link(title, wix_link)
        == "https://www.reddit.com/submit?url=https%3A%2F%2Fwww.guildmasterconsulting.com%2Fpost%2Forganizing-confluence-pages-how-to-conquer-your-mess-with-tags&title=Organizing%20Confluence%20Pages%3A%20How%20to%20Conquer%20Your%20Mess%20With%20Tags"
    )


def test_make_hackernews_link():
    title = "Organizing Confluence Pages: How to Conquer Your Mess With Tags"
    wix_link = outro.make_wix_link(title)

    assert (
        outro.make_hacker_news_link(title, wix_link)
        == "https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fwww.guildmasterconsulting.com%2Fpost%2Forganizing-confluence-pages-how-to-conquer-your-mess-with-tags&t=Organizing%20Confluence%20Pages%3A%20How%20to%20Conquer%20Your%20Mess%20With%20Tags"
    )


def test_outro_generator():
    generated_outro = outro.outro_generator(title=TITLE)

    assert (
        generated_outro
        == """**We're on a mission to make jobs suck less, one software management tip at a time. We need your help!**

- [Share to Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.guildmasterconsulting.com%2Fpost%2Forganizing-confluence-pages-how-to-conquer-your-mess-with-tags&title=Organizing%20Confluence%20Pages%3A%20How%20to%20Conquer%20Your%20Mess%20With%20Tags)
- [Share to Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fwww.guildmasterconsulting.com%2Fpost%2Forganizing-confluence-pages-how-to-conquer-your-mess-with-tags&t=Organizing%20Confluence%20Pages%3A%20How%20to%20Conquer%20Your%20Mess%20With%20Tags)

Do you want to stay up to date on the latest management tips to help your team stay productive?

Click "Subscribe to the Soapbox" below for more!

- [Follow us on Twitter](https://twitter.com/GuildmasterC)
- [Subscribe to our Podcast](https://www.youtube.com/results?search_query=guildmaster+consulting)
- [Follow us on LinkedIn](https://www.linkedin.com/company/guildmaster-consulting)"""
    )


def test_apostrophe_to_dash_wix_link():
    wix_link = outro.make_wix_link(
        title="How to Win Productivity Quickly at Work: Here's Guildmaster's Engineering Manager Job Description"
    )

    assert (
        wix_link
        == "https://www.guildmasterconsulting.com/post/how-to-win-productivity-quickly-at-work-here-s-guildmaster-s-engineering-manager-job-description"
    )


def test_apostrophe_to_dash_integration():
    """Wix replaces apostrophes with dashes in its title"""
    generated_outro = outro.outro_generator(
        title="How to Win Productivity Quickly at Work: Here's Guildmaster's Engineering Manager Job Description"
    )

    assert (
        generated_outro
        == """**We're on a mission to make jobs suck less, one software management tip at a time. We need your help!**

- [Share to Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.guildmasterconsulting.com%2Fpost%2Fhow-to-win-productivity-quickly-at-work-here-s-guildmaster-s-engineering-manager-job-description&title=How%20to%20Win%20Productivity%20Quickly%20at%20Work%3A%20Here%27s%20Guildmaster%27s%20Engineering%20Manager%20Job%20Description)
- [Share to Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fwww.guildmasterconsulting.com%2Fpost%2Fhow-to-win-productivity-quickly-at-work-here-s-guildmaster-s-engineering-manager-job-description&t=How%20to%20Win%20Productivity%20Quickly%20at%20Work%3A%20Here%27s%20Guildmaster%27s%20Engineering%20Manager%20Job%20Description)

Do you want to stay up to date on the latest management tips to help your team stay productive?

Click "Subscribe to the Soapbox" below for more!

- [Follow us on Twitter](https://twitter.com/GuildmasterC)
- [Subscribe to our Podcast](https://www.youtube.com/results?search_query=guildmaster+consulting)
- [Follow us on LinkedIn](https://www.linkedin.com/company/guildmaster-consulting)"""
    )
