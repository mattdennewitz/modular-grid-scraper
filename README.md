# modular grid scraper

## Installation

First, clone this repository

```shell
$ git clone https://github.com/mattdennewitz/modular-grid-scraper.git
$ cd modular-grid-scraper
```

Then, install its dependencies via `pipenv`

```shell
$ pipenv install
```

## Usage

Run via `pipenv`, exporting results as a JSON file:

```
$ pipenv run scrapy crawl modulargrid -o mod-grid-inventory.json
```

## Exported fields

- Manufacturer name
- Product name
- Tags
- Price (USD)
- URL
