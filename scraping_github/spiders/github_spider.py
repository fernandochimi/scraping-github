from os import path

import scrapy
from scrapy import Request


class QuotesSpider(scrapy.Spider):
    name = "scraping_github"
    base_path = path.dirname(__file__)
    file_path = path.abspath(path.join(
        base_path, "..", "..", "repositories.txt"))

    start_urls = ['https://github.com/' + repo.rstrip('\n')
                  for repo in open(file_path)]

    def parse(self, response):
        author_name = response.xpath(
            "//span[@class='author']/a[@class='url fn']/text()").\
            extract_first()
        project_name = response.xpath(
            "//strong/a/text()").extract_first()
        project_items = response.xpath("//tr[@class='js-navigation-item']")

        for item in project_items:
            file_or_folder = item.xpath(".//a/text()").extract_first()
            relative_path = item.xpath(".//a/@href").extract_first()
            absolute_path = response.urljoin(relative_path)
            yield Request(absolute_path,
                          callback=self.parse_details,
                          meta={"project_name":
                                author_name + "/" + project_name,
                                "file_or_folder": file_or_folder,
                                "url": absolute_path},
                          dont_filter=True)

    def parse_details(self, response):
        file_or_folder = response.meta.get("file_or_folder")
        project_name = response.meta.get("project_name")
        url = response.meta.get("url")
        info = response.xpath("//div[@class='file-info']/text()").extract()

        if not info:
            yield Request(url, callback=self.parse)
        else:
            lines = info[0].strip()
            _bytes = info[1].strip()

            yield {
                "file_or_folder": file_or_folder,
                "project_name": project_name,
                "lines": lines,
                "bytes": _bytes
            }
