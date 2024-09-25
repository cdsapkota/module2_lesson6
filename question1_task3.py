reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

def summary(reviews):
    for review in reviews:
        review_split = review.split()
        
        review_summary = review[0:30]
        review_summary_split = review_summary.split()

        last_word = review_split[len(review_summary_split)-1]
        review_summary_split[-1] = last_word

        final_review = " ".join(review_summary_split) + "..."

        print(final_review)



summary(reviews)