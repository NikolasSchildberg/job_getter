# job_getter
"Baby-level" web scraper with python and data processer with pandas.

It uses the *requests* library for importing an HTML from a webpage (in this case, job postings on the city hall of the town of Ilhabela-SP, in Brazil).

Then, data is parsed using *BeautifulSoup4*, and desired fields are processed using *pandas*, applying some filters.

## Result
One interested in those filters can access this data in desired format by quickly executing *jobs_getter.py* from the *CLI*, instead of browsing to the website and not finding any filters to apply on data (which unfortunately is the case for their website).
