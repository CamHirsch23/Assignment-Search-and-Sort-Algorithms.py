"""
Module for sorting videos using merge sort and providing a Flask API endpoint.
"""

import glob
from flask import Flask, jsonify, request

app = Flask(__name__)

def merge_sort(arr):
    """
    Sorts a list of videos based on their titles using the merge sort algorithm.
    
    Args:
        arr (list): List of videos, where each video is a dictionary with a 'title' key.
    
    Returns:
        list: Sorted list of videos.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i]['title'] < right[j]['title']:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


@app.route('/sort_videos', methods=['POST'])
def sort_videos():
    """
    API endpoint to sort a list of videos based on their titles.
    
    Returns:
        JSON: Sorted list of videos.
    """
    videos = request.json['videos']
    sorted_videos = merge_sort(videos)
    return jsonify(sorted_videos)


def merge_files(output_file, *input_files):
    """
    Merges multiple Python files into a single file.
    
    Args:
        output_file (str): The name of the output file.
        input_files (list): List of input files to be merged.
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for fname in input_files:
            with open(fname, encoding='utf-8') as infile:
                outfile.write(infile.read() + '\n')


if __name__ == '__main__':
    files = glob.glob('*.py')
    merge_files('combined_script.py', *files)

    app.run(debug=True)
