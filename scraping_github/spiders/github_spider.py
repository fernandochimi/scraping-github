import scrapy
from scrapy import Request


class QuotesSpider(scrapy.Spider):
    name = "scraping_github"
    start_urls = [
        'https://github.com/fernandochimi/medical-appointment',
        # 'https://github.com/fernandochimi/scraping-github'
    ]

    def parse(self, response):
        project_items = response.xpath(
            "//tbody/tr[@class='js-navigation-item']")

        for item in project_items:
            file_or_folder = item.xpath(".//a/text()").extract_first()
            print("FAIOUOUFOUDER", file_or_folder)
            relative_path = item.xpath(".//a/@href").extract_first()
            absolute_path = response.urljoin(relative_path)
            yield Request(absolute_path, callback=self.parse_details,
                          meta={"file_or_folder": file_or_folder})

    def parse_details(self, response):
        file_or_folder = response.meta.get("file_or_folder")
        info = response.xpath("//div[@class='file-info']/text()").extract()

        if not info:
            relative_info = response.xpath(
                "//a[@class='js-navigation-open']/@href|"
                "tr[not(@class='up-tree js-navigation')]")[1:].extract_first()
            absolute_info = response.urljoin(relative_info)
            yield Request(absolute_info, callback=self.parse)
        else:
            lines = info[0].strip()
            _bytes = info[1].strip()

            yield {
                "file_or_folder": file_or_folder,
                "lines": lines,
                "bytes": _bytes
            }
