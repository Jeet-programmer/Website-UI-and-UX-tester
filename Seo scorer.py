import requests
from bs4 import BeautifulSoup
import re

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

def extract_keywords(html_content):
    # Remove HTML tags
    clean_text = re.sub('<[^<]+?>', ' ', html_content)
    # Tokenize and remove punctuation
    words = re.findall(r'\b\w+\b', clean_text.lower())
    # Create a dictionary to count word occurrences
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    # Sort the words by frequency
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    # Extract top 10 keywords
    top_keywords = [word for word, count in sorted_words[:10]]
    return top_keywords

def calculate_score(html_content, keywords):
    keyword_density = sum(html_content.lower().count(keyword.lower()) for keyword in keywords)
    total_words = len(re.findall(r'\b\w+\b', html_content.lower()))
    score = (keyword_density / total_words) * 100
    return min(score, 100)  # Ensure score does not exceed 100

# Example usage
url = "https://lumaticai.com"
def generate_SEO_score(url):
    html_content = get_html_content(url)
    if html_content:
        keywords = extract_keywords(html_content)
        # print("Extracted Keywords:", keywords)
        score = calculate_score(html_content, keywords)
        print("SEO Score:", score)
        return score
generate_SEO_score(url)