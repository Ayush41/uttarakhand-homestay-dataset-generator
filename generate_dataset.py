import pandas as pd
import numpy as np
import random 
from faker import Faker 
from datetime import datetime, timedelta

fake = Faker("en_IN")


NUM_REVIEWS = 3500


districts = [
    # uttarakhands all districts
    "Nainital",
    "Almora",
    "Mukteshwar",
    "Kausani",
    "Ranikhet",
    "Chamoli",
    "Uttarkashi",
    "Pithoragarh",
    "Tehri Garhwal",
    "Rudraprayag"

]

homestays = [
    # homestay names
    "Mountain View Homestay",
    "Himalayan Nest",
    "Pine Valley Retreat",
    "Eco Village Stay",
    "Snow Peak Homestay",
    "Riverstone Cottage",
    "Forest Edge Homestay",
    "Valley Breeze Retreat",
    "Nature Trails Stay",
    "Green Hills Homestay",
    "Oakwood Cottage",
    "Sunrise Eco Stay",
    "Cloud View Homestay",
    "Wildflower Retreat",
    "Lake View Cottage"
]

positive_reviews = [
    "Amazing hospitality and very friendly hosts.",
    "Beautiful mountain views and peaceful atmosphere.",
    "Excellent local food and authentic village experience.",
    "Clean rooms and wonderful service.",
    "Perfect place for eco tourism and nature lovers.",
    "The hosts made us feel like family.",
    "Outstanding experience with great trekking options.",
    "Loved the scenic surroundings and fresh air.",
    "Great value for money and comfortable stay.",
    "One of the best homestays we have visited."
]

neutral_reviews = [
    "Overall a decent stay with basic facilities.",
    "The location was nice but amenities were average.",
    "Good experience but room maintenance can improve.",
    "Comfortable stay though food options were limited.",
    "The property was satisfactory for a short visit."
]

negative_reviews = [
    "Room cleanliness needs improvement.",
    "WiFi connectivity was poor during the stay.",
    "Food quality did not meet expectations.",
    "Service response was slower than expected.",
    "Property maintenance needs attention.",
    "The room was smaller than shown in photos.",
    "Road access to the homestay was difficult.",
    "Limited facilities for the price charged."
]

review_topics = [
    "Hospitality",
    "Food",
    "Cleanliness",
    "Location",
    "Scenic Beauty",
    "Accessibility",
    "Value for Money",
    "Amenities",
    "Eco Tourism",
    "Trekking"   
]


guest_types = [
    "Solo Traveler",
    "Couple",
    "Family",
    "Friends Group",
    "Adventure Traveler"
]

records = []

# Generate Synthetic Dataset
for review_id in range(1, NUM_REVIEWS + 1):

    district = random.choice(districts)
    homestay = random.choice(homestays)

    sentiment_choice = random.choices(
        ["Positive", "Neutral", "Negative"],
        weights=[65, 15, 20]
    )[0]

    if sentiment_choice == "Positive":
        review_text = random.choice(positive_reviews)
        rating = random.choice([4, 5])

    elif sentiment_choice == "Neutral":
        review_text = random.choice(neutral_reviews)
        rating = 3

    else:
        review_text = random.choice(negative_reviews)
        rating = random.choice([1, 2])

    review_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    records.append({
        "review_id": review_id,
        "homestay_id": random.randint(1001, 1050),
        "homestay_name": homestay,
        "district": district,
        "state": "Uttarakhand",
        "guest_type": random.choice(guest_types),
        "rating": rating,
        "review_text": review_text,
        "sentiment": sentiment_choice,
        "review_topic": random.choice(review_topics),
        "review_date": review_date,
        "host_response": random.choice(["Yes", "No"]),
        "stay_duration_days": random.randint(1, 10),
        "booking_channel": random.choice([
            "Google",
            "Direct",
            "Tripadvisor",
            "Referral",
            "Travel Agency"
        ])
    })

# Dataframe records and convert to CSV
df = pd.DataFrame(records)

df.to_csv(
    "Uttarakhand_HomeStay_Reviews.csv"
    index = False 
)

# Print df head and len of reviews

print(df.head())
print(f"\n\nGenerated {len(df)} reviews")