# Author: Jeremiah Jackson-Williams
#
# Email: rainai.inc@gmail.com # distorted.corp@gmail.com
# Copyrights: Rainai Inc. @2025
#

import requests
from bs4 import BeautifulSoup

class vectorize:
    def __init__(self, target_url):
        # Ensure target_url includes protocol for requests if not provided
        if not target_url.startswith(('http://', 'https://')):
            self.target_url = "https://" + target_url # Default to HTTPS
        else:
            self.target_url = target_url

        self.session = requests.Session() # Use a session for persistent connections (good practice)
        self.robots_data = {} # To store robots.txt data
        self.raw_html_fetched = "" # To store the main page HTML

    def shift0(self):
        # This method could be for initial setup or baseline checks.
        # For now, it simply returns self to allow method chaining.
        return self

    def reconMata(self):
        """
        Performs reconnaissance: fetches robots.txt and the main page HTML.
        Populates self.robots_data and self.raw_html_fetched.
        Returns a tuple: (stats_data_dict, raw_html_content_string)
        where stats_data_dict contains robots.txt 'Disallow' paths.
        """
        stats_data_dict = {} # This will be the dictionary returned for other data (like robots.txt)

        # 1. Fetch robots.txt
        robots_url = self.target_url.rstrip('/') + '/robots.txt'
        try:
            print(f"Fetching robots.txt from: {robots_url}")
            robots_response = self.session.get(robots_url, timeout=10)
            robots_response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

            if robots_response.status_code == 200:
                robots_content = robots_response.text
                # Parse robots.txt for 'Disallow' directives
                disallow_count = 0
                for line in robots_content.splitlines():
                    line_stripped = line.strip()
                    if line_stripped.lower().startswith('disallow:'):
                        path = line_stripped.split(':', 1)[1].strip()
                        # Add to stats_data_dict with a ROBOTS- prefix and an incrementing ID
                        stats_data_dict[f"ROBOTS-{disallow_count}"] = path
                        disallow_count += 1
                print(f"Successfully fetched and parsed robots.txt for {self.target_url}. Found {disallow_count} disallow rules.")
            else:
                print(f"robots.txt not found or inaccessible for {self.target_url}. Status: {robots_response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching robots.txt for {self.target_url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during robots.txt processing: {e}")

        # 2. Fetch main page HTML
        try:
            print(f"Fetching main page HTML from: {self.target_url}")
            main_page_response = self.session.get(self.target_url, timeout=15)
            main_page_response.raise_for_status() # Raise an exception for bad status codes
            self.raw_html_fetched = main_page_response.text
            print(f"Successfully fetched main page HTML for {self.target_url}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching main page HTML for {self.target_url}: {e}")
            self.raw_html_fetched = "" # Ensure it's empty on failure
        except Exception as e:
            print(f"An unexpected error occurred during main page HTML fetch: {e}")
            self.raw_html_fetched = ""

        # Return the collected stats_data_dict (for robots.txt) AND the raw HTML content
        return (stats_data_dict, self.raw_html_fetched)

# Example usage (for testing spectralComFreeVersion.py independently):
if __name__ == "__main__":
    target = "http://example.com"
    print(f"\n--- Testing spectralComFreeVersion for {target} ---")
    vec_instance = vectorize(target)
    stats, html = vec_instance.shift0().reconMata()

    print("\n--- statsDatOut (Robots.txt data) from reconMata ---")
    import json
    print(json.dumps(stats, indent=2))

    print("\n--- Raw HTML (first 500 chars) ---")
    print(html[:500])
    if len(html) > 500:
        print("...")
    print("-----------------------------------\n")

    target_apple = "https://www.apple.com"
    print(f"\n--- Testing spectralComFreeVersion for {target_apple} ---")
    vec_apple_instance = vectorize(target_apple)
    stats_apple, html_apple = vec_apple_instance.shift0().reconMata()
    print("\n--- statsDatOut (Robots.txt data) from reconMata (Apple) ---")
    print(json.dumps(stats_apple, indent=2))
    print("\n--- Raw HTML (first 500 chars) (Apple) ---")
    print(html_apple[:500])
    if len(html_apple) > 500:
        print("...")
    print("-----------------------------------\n")
