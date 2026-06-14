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

# Dataframe records and convert to CSV

# Print df head and len of reviews
