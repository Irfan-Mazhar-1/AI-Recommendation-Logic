def calculate_similarity(preferences, item_interests):
    """Return a percentage showing how many user preferences match an item."""
    if not preferences:
        return 0.0

    matched = preferences.intersection(item_interests)
    return (len(matched) / len(preferences)) * 100


def get_recommendations(preferences, items):
    """Return matching items ranked from highest to lowest similarity."""
    recommendations = []

    for item in items:
        item_interests = set(item["interests"])
        matched = preferences.intersection(item_interests)
        score = calculate_similarity(preferences, item_interests)

        if matched:
            recommendations.append(
                {
                    **item,
                    "score": score,
                    "matched": sorted(matched),
                }
            )

    return sorted(
        recommendations,
        key=lambda item: (-item["score"], item["name"]),
    )
