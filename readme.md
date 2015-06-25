#National Park Service unit code scraper

After looking at several interal list park units, I elected to scrape them from www.nps.gov

1) copy the list of unitcodes and full names from the source view of http://www.nps.gov/findapark/index.htm

2) Clean up the list with simple search and replace commands in your favorite editor (or sed commands if you are *nix dude)

3) The results of step 2 (as a list of tab separated values) is cached in weblist.tsv

4) Run this file through url_scraper.py to generate list.json

5) Clean up any 404 errors by hand
