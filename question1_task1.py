reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for keyword in keywords:
        if keyword in review.lower():
            new_review = review.replace(keyword, keyword.upper()).replace(keyword.capitalize(), keyword.upper())
            print(new_review)
