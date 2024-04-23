from scrapy import Spider, Request
from scrapy.exceptions import CloseSpider

class GoodreadsQuotesSpider(Spider):
    name = "goodreads_quotes"
    allowed_domains = ["goodreads.com"]
    start_urls = ["https://www.goodreads.com/quotes"]
    max_pages = 50  # Maximum number of pages to crawl
    max_depth = 2  # Maximum depth to crawl
    count = 0  # Counter to keep track of the number of pages crawled

    def parse(self, response):
        quotes_html = "<html><head><title>Goodreads Quotes</title></head><body>"
        self.count += 1
        if self.count > self.max_pages:
            raise CloseSpider('Reached maximum number of pages')
        if response.meta['depth'] > self.max_depth:
            raise CloseSpider('Reached maximum depth')

        quotes = response.css('div.quote')
        for quote in quotes:
            text = quote.css('div.quoteText::text').get().strip()
            author = quote.css('span.authorOrTitle::text').get().strip()
            tags = [tag.strip() for tag in quote.css('div.greyText a::text').getall()]
            quotes_html += f"<p><strong>{text}</strong> - {author}<br>Tags: {', '.join(tags)}</p>"
        
        quotes_html += "</body></html>"
        with open('goodreads_quotes.html', 'w', encoding='utf-8') as f:
            f.write(quotes_html)

        # Follow pagination links
        for next_page in response.css('.next_page'):
            yield Request(url=response.urljoin(next_page.attrib['href']), callback=self.parse)
