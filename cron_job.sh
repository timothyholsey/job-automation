#!/bin/bash

# This script runs the job scrapers every 6 hours

# Define the path to the scripts
directory="/path/to/scripts"

# Run the Fiverr scraper
cd "$directory" && python3 fiverr_scraper.py

# Run the Craigslist scraper
cd "$directory" && python3 craigslist_scraper.py

# Run the Mystery Shopping scraper
cd "$directory" && python3 mystery_shopping_scraper.py

# Schedule this script to run every 6 hours using cron
# Add the following line to your crontab (crontab -e):
# 0 */6 * * * /path/to/cron_job.sh
