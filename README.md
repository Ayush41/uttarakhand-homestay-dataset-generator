# Uttarakhand Homestay Dataset Generator

## Overview
This repository provides a compact Python utility that generates a synthetic review dataset for Uttarakhand homestays and eco-tourism properties. It is built for analytics teams, product owners, and data engineers who need a clean dataset for BI, SQL modeling, and NLP experimentation.

The generated dataset includes realistic review metadata, sentiment labels, guest segments, booking channels, and district-level geographic context.

# Published Kaggle Dataset
🔗https://www.kaggle.com/datasets/ayushraj41/uttarakhand-homestay-reviews-dataset

## Key Use Cases
- BI dashboard prototyping
- Exploratory analytics for hospitality and tourism
- Sentiment analysis and NLP model training
- Data engineering and reporting demonstrations

## Output Dataset
The script produces `Uttarakhand_HomeStay_Reviews.csv` with the following fields:

| Column | Purpose |
| --- | --- |
| `review_id` | Unique review identifier |
| `homestay_id` | Property identifier |
| `homestay_name` | Homestay property name |
| `district` | Geographic analysis dimension |
| `state` | Static value `Uttarakhand` |
| `guest_type` | Traveler segment |
| `rating` | Review rating KPI |
| `review_text` | Raw review text for NLP and sentiment analysis |
| `sentiment` | Synthetic sentiment label |
| `review_topic` | Theme/topic label |
| `review_date` | Review timestamp |
| `host_response` | Host response indicator |
| `stay_duration_days` | Stay duration metric |
| `booking_channel` | Booking acquisition channel |

## Installation

```bash
cd /workspaces/uttarakhand-homestay-dataset-generator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python generate_dataset.py
```

The generated file will be written to:

```bash
Uttarakhand_HomeStay_Reviews.csv
```

## Requirements

- Python 3.11+ recommended
- `pandas`
- `numpy`
- `Faker`

## Notes for Data Teams

- The dataset is synthetic and intended for prototyping, analytics, and demos.
- Sentiment and rating values are weighted to create a realistic distribution of guest feedback.
- This dataset is a good starting point for building dashboards, classification models, or SQL analytics pipelines.
- You can extend the script with additional business fields like room type, booking value, or campaign source.

## Analytical Model Recommendation

- `homestays` as the property dimension table
- `reviews` as the fact table
- `sentiment_analysis` as a derived metrics or ML output layer
