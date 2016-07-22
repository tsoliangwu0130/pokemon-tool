# Pokémon-Tool

This Pokémon tool is for personal practice purpose project.<br/>
All Pokémon data right reserved by the [original author (Pokémon Database)](http://pokemondb.net/).

### Installation

[Scrapy](http://scrapy.org/) installed is necessary. Simply run `pip install scrapy` to install it.

### Usage

#### crawlers

Run the following command to retrieve Pokémons data and save to the database:
	
	`scrapy crawl <crawlerName>`

or run the following command to retrieve Pokémons data and restore as a json file:
	
	`scrapy crawl <crawlerName> -o <outputName>.json -t json`
