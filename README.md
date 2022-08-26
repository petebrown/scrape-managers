# scrape-managers

This repo contains the code that scrapes the names of Tranmere managers and the dates they were in post. The results are saved in output/managers_df.csv. This repo uses GitHub Actions to check for updates every day at 12pm.

Prerequisites are `bs4`, `pandas` and `requests`

To run use `python scrape-managers.py`