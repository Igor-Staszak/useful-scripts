# Pharmacy medicine stock checker

Python script that checks the availability of a desired medicine in any pharmacy nearby requested location.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting the URLs for checking](#getting-the-urls-for-checking)
  - [gdziepolek.pl](#gdziepolekpl)
  - [ktomalek.pl](#ktomalekpl)
- [Usage](#usage)
- [Potential improvements](#potential-improvements)

## Prerequisites

- `playwright` installed
- `BeautifulSoup` installed

## Getting the URLs for checking

In order to check the websites you need to prepare a URLs.

### gdziepolek.pl

Go to the website, insert your location, medicine name and get the URL from the location bar.

### ktomalek.pl

Go to the website, insert your location, medicine name, copy the URL by pressing the button `Udostępnij wyszukiwanie`.

## Usage

1. Provide the URLs as the function parameters:
   ```bash
   check_ktomalek("url1")
   check_gdziepolek("url2")
   ```
2. Optionally, place the script in the crontab so it checks every X minutes.

## Potential improvements

In the future, the script can be easily improved by for example adding a push notification (via email, discord message, etc.).
