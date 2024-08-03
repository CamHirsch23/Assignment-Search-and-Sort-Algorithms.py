from flask import Flask, request, jsonify

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]


def binary_search(video_titles, search_query):
    left = 0
    right = len(video_titles) - 1
    matches = []

    while left <= right:
        mid = (left + right) // 2
        if video_titles[mid] == search_query:
            matches.append(video_titles[mid])
            # Uncomment the following line if you want to find all matching videos
            # and not just the first occurrence.
            # left = mid + 1
            break
        elif video_titles[mid] < search_query:
            left = mid + 1
        else:
            right = mid - 1

    return matches


@app.route('/search', methods=['GET'])
def search_videos():
    search_query = request.args.get('query')

    # Perform binary search
    matches = binary_search(video_titles, search_query)

    return jsonify({'results': matches})


if __name__ == '__main__':
    app.run()
