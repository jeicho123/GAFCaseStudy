# GAF Case Study

A Python-based web scraping and analysis tool for gathering and processing data.

## Setup

1. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

The project consists of two main scripts:

- `scrape.py`: Web scraping script for data collection
- `process.py`: Data processing and analysis script

Run the scripts in sequence:
```
python scrape.py
python process.py
```

## Output

Results are saved in JSON format:
- `companies.json`: Raw scraped data
- `analysis_results_*.json`: Processed analysis results
