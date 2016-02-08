# UN Habitat urbaninfo API Collector

[HDX](https://data.hdx.rwlabs.org/) collector for the [urbaninfo API](http://www.devinfo.org/urbaninfo/libraries/aspx/RegDataQuery.aspx).

## Introduction

This collector operates in the following way:

- Downloads a json file of climate data for location
- Parses and flattens nested data
- Adds new records to the database `data` table

[View the live data](https://data.hdx.rwlabs.org/dataset/urbaninfo-indicators-2011)

## Setup

    pip install -r requirements.txt

*local*

    manage setup

*ScraperWiki Box*

    manage -m Scraper setup

## Usage

*local*

    manage run

*ScraperWiki Box*

    manage -m Scraper run

The results will be stored in a SQLite database `scraperwiki.sqlite`.
