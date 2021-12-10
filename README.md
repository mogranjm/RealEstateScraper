# WebScraper

So I tried to scrape RealEstate.com.au but they've got some kind of powerful scrape-blocker that runs when you hit their frontdoor and only redirects human requests. But ONLY for queried pages (i.e. house search pages). Search results are rendered when a human is running the browser, but anything from a simple GET request to a Selenium webdriver configured for relative anonymity returns an HTML response that only contains a <script> tag that references a heavily obfuscated JS file that I couldn't be bothered to break down. I can only assume that the JS generates a cookie, or detects a non-human request in some other way.

I've only checked realestate dot com dot au slash buy, but I assume that the rent endpoint would produce the same results.

I discovered that Domain is queriable using the requests module.
