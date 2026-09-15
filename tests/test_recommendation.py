from recommendation import calculate_similarity, get_recommendations


def test_similarity_with_matches():
    preferences = {"python", "ai", "programming"}
    interests = {"python", "ai", "data"}
    assert calculate_similarity(preferences, interests) == 66.66666666666666


def test_similarity_with_no_matches():
    preferences = {"python", "ai"}
    interests = {"design", "art"}
    assert calculate_similarity(preferences, interests) == 0


def test_empty_preferences():
    assert calculate_similarity(set(), {"python"}) == 0


def test_recommendations_are_ranked():
    preferences = {"python", "ai", "programming"}
    items = [
        {"name": "One", "category": "A", "interests": {"python"}},
        {"name": "Two", "category": "A", "interests": {"python", "ai", "programming"}},
        {"name": "Three", "category": "A", "interests": {"design"}},
    ]

    results = get_recommendations(preferences, items)

    assert [item["name"] for item in results] == ["Two", "One"]
    assert results[0]["score"] == 100
    assert results[0]["matched"] == ["ai", "programming", "python"]


def test_no_matching_items():
    preferences = {"music"}
    items = [
        {"name": "One", "category": "A", "interests": {"python"}},
    ]

    assert get_recommendations(preferences, items) == []
