# National Park Service Unit Code list generator

This project creates a JSON list (actually a JSON object wrapped in a javascript declaration)
of NPS unit codes that can be used to create headers in html as
typically seen on a park page at www.nps.gov. The list needs the full name and state codes for each
unit code. After looking at several internal and external lists (examples `wikipedia.txt` and
`npslist.tsv`), none of which were complete,
I elected to scrape them from www.nps.gov.  This also assures me that the output matches the source
I was trying to emulate.  The output of this process (`units.js`) is used in the custom NPS storymap templates
([Map Tour](https://github.com/nationalparkservice/storymap-tour/blob/master/MapTour/src/app/storymaps/ui/header/units.js),
[Map Series](https://github.com/nationalparkservice/storymap-series/blob/master/src/app/storymaps/NpsUnits.js),
and [Shortlist](https://github.com/nationalparkservice/storymap-shortlist/blob/master/oldapp/units.js))

A simpler solution might now be possible with the [NPS API](https://www.nps.gov/subjects/developer/api-documentation.htm)

## Build

1) Copy the list of unit codes and full names from the source view of http://www.nps.gov/findapark/index.htm.
2) Clean up the list in a text editor until it resembles `weblist.tsv` (cached from the last time this
process was run).
3) Edit the paths of the input/output files in `url_scraper.py` to match your file system.
4) Run `url_scraper.py` (works with python 2.7 or 3.x) to generate an output file (`units.js`).
4) Clean up any 404 errors (printed to the console) by hand editing the output file.

**IMPORTANT** Like any URL scrapper, it is highly dependent on the structure of the html
in the files being scraped.  This script worked when written, but it will generate incorrect
output if the html changes (highly likely over time).  The code is pretty simple,
so it shouldn't be too hard to adapt in the future, provided the park pages still display
the data required.

## Deploy

Copy the unit.js code to the story map files lined above, or embed in your own web page.
