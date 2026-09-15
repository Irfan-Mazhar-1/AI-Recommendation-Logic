from recommendation import get_recommendations
from data import ITEMS


def get_user_preferences():
    print("AI Recommendation System")
    print("=" * 24)
    print("Available interests:")

    all_interests = sorted(
        {interest for item in ITEMS for interest in item["interests"]}
    )
    print(", ".join(all_interests))

    while True:
        raw = input("\nEnter your interests (comma-separated): ").strip()

        preferences = {
            value.strip().lower()
            for value in raw.split(",")
            if value.strip()
        }

        if preferences:
            return preferences

        print("Please enter at least one interest.")


def display_recommendations(recommendations):
    print("\nRecommended Items")
    print("-" * 24)

    if not recommendations:
        print("No matching recommendations found.")
        return

    for number, item in enumerate(recommendations, start=1):
        print(f"{number}. {item['name']}")
        print(f"   Category: {item['category']}")
        print(f"   Match: {item['score']:.0f}%")
        print(f"   Matched interests: {', '.join(item['matched'])}")


def main():
    preferences = get_user_preferences()
    recommendations = get_recommendations(preferences, ITEMS)
    display_recommendations(recommendations)


if __name__ == "__main__":
    main()
