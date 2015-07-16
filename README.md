## WFP VAM API Collector
Collector for the [WFP VAM API](http://reporting.vam.wfp.org/api/).

## Usage

If you are on an Unix machine run:
```bash
$ make run
```

Or you can run directly using Python:
```bash
$ python scripts/wfp_collect/
```
The results will be stored in CSV files, JSON files, and / or a SQLite database called "scraperwiki.sqlite".


You will also need to install the dependencies and setup the database schema:

```terminal
$ make setup
```

## Cleaning Data
The modified GAUL boundary set provided by the VAM unit contains around 50k administrative codes. However, the provision starts at the admin 2 level, meaning that codes for amin 0 and admin 1 don't have individual records. We need those records in order to query for admin 1 units or admin 0 units without specifying a further level of disaggregation. The `clean_admin_codes.R` script solves that issue by creating those missing records. To run do:

```bash
$ Rscript code/clean_admin_codes.R
```

A new CSV file titled `modified_admin_units.csv` will be generated to the [config](config/) directory.

## Making Queries
The queries seem to be unique. That is, an user will have to make a large number of queries (*hundreds of thousands*) in order to collect the complete database. This scraper was designed to make those queries automatically and store the resulting data.

# API Design
The current API design imposes on the user the assumption that he knows a considerable amount of information before issuing queries. Users have to know exactly the combination of administrative units, indicator type IDs, and other variables in order to get the series she is interested on. In sum, the API isn't designed for exploration.

To go around this issue, this scraper issues queries using the combination of available query parameters. Considering that there are around 60 thousand locations available, the combination of variables result in nearly one million queries. This is inefficient and costly in computational terms.

## Parallel Processing
To be written.
