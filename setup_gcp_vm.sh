#!/bin/bash

# Update and install necessary packages
sudo apt-get update && sudo apt-get install -y nodejs npm

# Install Puppeteer and Cheerio globally
sudo npm install -g puppeteer cheerio

# Install cron
sudo apt-get install -y cron

# Set up cron jobs
(crontab -l 2>/dev/null; echo "0 */6 * * * /path/to/scraper_fiverr.js") | crontab -
(crontab -l 2>/dev/null; echo "0 */6 * * * /path/to/scraper_craigslist.js") | crontab -
(crontab -l 2>/dev/null; echo "0 */6 * * * /path/to/scraper_mystery_shopping.js") | crontab -
