# Pokémon-Tool
This Pokémon tool is for personal practice purpose project.<br/>
All Pokémon data right reserved by the [original author (Pokémon Database)](http://pokemondb.net/).

### Installation
[Scrapy](http://scrapy.org/) installed is necessary. Simply run `pip install scrapy` to install it.

### Usage

#### crawlers
1. Run `scrapy crawl pokemon_crawler -o pokemon_crawler.json -t json` to retrieve Pokémons data and restore as a json file.
2. Run `scrapy crawl move_crawler -o move_crawler.json -t json` to retrieve Moves data and restore as a json file.
