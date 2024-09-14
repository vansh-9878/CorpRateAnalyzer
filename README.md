# CorpRateAnalyzer

**CorpRateAnalyzer** is a Python tool that fetches reviews of companies from Trustpilot.com using web crawling and calculates a star rating based on sentiment analysis. The tool uses the VADER (Valence Aware Dictionary) and sentiment analysis technique to convert review sentiments into a star rating on a scale of 1 to 5.

## Features

- Web crawling of company reviews from Trustpilot.
- Sentiment analysis of reviews using the VADER model.
- Conversion of sentiment scores into a 1-5 star rating.
- Easy to use: simply input the company name and get an aggregated rating.

## How it Works

1. The user provides the name of a company.
2. The program crawls the Trustpilot website to gather reviews for that company.
3. It processes the reviews using the VADER sentiment analyzer to determine the sentiment score.
4. The sentiment score is mapped to a 5-star rating system.
5. The tool returns the average rating for the company based on the reviews.

## Requirements

- Python 3.x
- Required Libraries:
  - `requests`
  - `beautifulsoup4`
  - `vaderSentiment`

You can install the necessary libraries using the following command:

```bash
pip install requests beautifulsoup4 vaderSentiment
```

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/CorpRateAnalyzer.git
```
Navigate to the project directory:
```bash
cd CorpRateAnalyzer
```
Install the required Python packages:
```bash
pip install requests beautifulsoup4 vaderSentiment
```
Usage
To use the program, simply run the Python script and input the company's name when prompted:

```bash
python webCrawler.py
```


## Limitations
- The tool relies on Trustpilot reviews, which may not cover all companies.
- It assumes that all reviews are in English (VADER performs best on English text).
- Web crawling might be limited by Trustpilot's anti-scraping measures, and with respect to their robots.txt rules.

