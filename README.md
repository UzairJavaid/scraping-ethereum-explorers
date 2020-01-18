# scraping-ethereum-explorers
A python-based scraper that scrapes required data for Ethereum addresses from blockchain explorers using Scrapy, which is an open source and collaborative framework for extracting the data you need from websites. Please see the link for further details:
```
https://scrapy.org/
```

# structure
The crawler is coded for n number of addresses, which enables it to crawl as many websites to be queried for an address as you want. I have included a file (keys.csv) that contains a list of 670 addresses, which is used to query these explorers:
```
https://blockchair.com/
https://www.blockchain.com/
```
Primarily, I opted to use blockchain.com since it didn't give any HTTP error.

# installation and Usage
You need to install Scrapy first before running the spider. Please see the link on how-to-install Scrapy:
```
https://docs.scrapy.org/en/latest/intro/install.html
```
To run the spider, clone the repo and go to directory:
```
$ git clone https://github.com/UzairJavaid/scraping-ethereum-explorers
$ cd .../scraping-ethereum-explorers
$ scrapy runspider ccs -o data.csv
```
