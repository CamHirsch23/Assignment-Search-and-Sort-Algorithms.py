Task 3: Testing the Video Search Functionality

To test the video search functionality, you can use tools like Postman or cURL to send requests to the API endpoint created in Task 2. Send different search queries as parameters in the requests to verify the correctness and efficiency of the search algorithm.
For example, if you're running the Flask API locally on your machine, you can send a GET request to http://localhost:5000/search?query=Artificial%20Intelligence to search for videos with the title "Artificial Intelligence". The response should contain the matching videos in the "results" field.
Make sure to test the API with various search queries, including both existing and non-existing videos, to ensure that it returns the expected results and handles edge cases appropriately.
Please note that the provided code snippets are meant to serve as examples and may require additional modifications based on your specific implementation requirements.
