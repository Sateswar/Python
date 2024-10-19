from serpapi import GoogleSearch
import json

def scrape_google_results(query):
    try:
        # Create a GoogleSearch object
        search = GoogleSearch({"q": query})

        # Get search results
        results = search.get_dict()

        return results

    except Exception as e:
        print("An error occurred:", str(e))
        return {}

def save_results_to_file(results, file_name):
    try:
        # Save results to a JSON file
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        print("Results saved to", file_name)

    except Exception as e:
        print("An error occurred while saving results:", str(e))

if __name__ == "__main__":
    # Replace 'YOUR_QUERY' with the search query you want to perform
    query = 'YOUR_QUERY'

    # Replace 'output.json' with the desired file name to save the results
    output_file = 'output.json'

    # Scrape Google search results
    results = scrape_google_results(query)

    # Save results to a JSON file
    save_results_to_file(results, output_file)
