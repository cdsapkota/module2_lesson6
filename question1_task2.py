reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def tally(reviews, positive_words, negative_words):
    positive_word_count = 0
    negative_word_count = 0
    for review in reviews:
        for word in positive_words:
            if word in review.lower():
                positive_word_count += 1
        for word in negative_words:
            if word in review.lower():
                negative_word_count += 1
        
    print(f"Positive word count is {positive_word_count}")
    print(f"Negative word count is {negative_word_count}")

tally(reviews, positive_words, negative_words)