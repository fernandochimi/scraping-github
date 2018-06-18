import scrapy


class QuotesSpider(scrapy.Spider):
    name = "scraping_github"
    start_urls = [
        'https://github.com/fernandochimi/medical-appointment'
    ]

    def parse(self, response):
        # project_name = {"project": (response.css(
        #     "h1.public .author a.url::text").extract_first().strip() +
        #     "/" + response.css("strong a::text").extract_first().strip())}

        for info in response.css("span.css-truncate a.js-navigation-open"):
            yield response.follow(info, self.parse_project_files)

    def parse_project_files(self, response):
        def extract_file(query):
            return response.css(query).extract_first().strip()

        def extract_info(query):
            return response.css(query).extract()

        file_name = extract_file("div.breadcrumb strong::text")
        info = extract_info("div.file-info::text")

        if not info:
            for item in response.css("span.css-truncate a.js-navigation-open"):
                yield response.follow(item, callback=self.parse_project_files)

        lines = info[0].strip()
        _bytes = info[1].strip()

        yield {
            "file": file_name,
            "lines": lines,
            "bytes": _bytes
        }
