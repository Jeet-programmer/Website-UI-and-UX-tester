import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
value = os.getenv('Insight')
def get_page_speed_insights(url):
    # Google PageSpeed Insights API endpoint
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    
    # Parameters for the API request
    params = {
        'url': url,
        'strategy': 'desktop',  # 'mobile' or 'desktop' strategy
        'key': value  # Replace 'YOUR_API_KEY' with your actual API key
    }
    
    try:
        # Making the API request
        response = requests.get(endpoint, params=params)
        data = response.json()
        
        # Checking if the request was successful
        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['error']['message']}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
# Example usage
url = "https://lumaticai.com"
page_speed_data = get_page_speed_insights(url)
if page_speed_data:
    print("PageSpeed Insights:")
    print("URL:", url)
    # print(page_speed_data)
    save_to_json(page_speed_data, 'data.json')
    # print("Data saved to data.json")
    A={
        "performance": page_speed_data['lighthouseResult']['categories']['performance']['score'],
        "accessibility": page_speed_data['lighthouseResult']['categories']['accessibility']['score'],
    }
    # print("First Contentful Paint:", page_speed_data['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['percentile'])
    # print("First Input Delay:", page_speed_data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['percentile'])
    # Add more insights as needed
