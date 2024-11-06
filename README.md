# Piazza-Scraper
Project to scrape all post data from Piazza, then analyze to try and find meaningful insights on problematic questions, wording, where students tend to struggle.

This project requires the following code files:
* scraper.py - this file handles pulling all the files from Piazza. This uses the Piazza API package here: https://github.com/hfaran/piazza-api. 
* login_info.py - this file stores variables required for scraper.py such as Piazza Email + Password + Piazza course code. I've added a file login_info_PH.py to show what this should look like but haven't uploaded my own because I don't want to give away my very valuable Piazza account info.
* analysis.py - this handles analysis of the data (WIP).

# How to use the script:
1. First, **input your email/password/desired course ID into the login_info.py file**. Ensure you save it.
2. **Run scraper.py.** This may take **~10-15 minutes** to run depending on the size of the Piazza. A good estimate is it'll take about **1 second per post**. The data will be saved into a .csv file in the same folder.
3. Run analysis.py on the CSV file. This can be run with **python analysis.py XXX.csv** where this last filename is the name of the CSV file.
