# Author: Jeremiah Jackson-Williams
#
# Email: rainai.inc@gmail.com # distorted.corp@gmail.com
# Copyrights: Rainai Inc. @2025
#

import os
import subprocess
import sys
from time import sleep, time
from bs4 import BeautifulSoup # Import BeautifulSoup for HTML parsing

# Assuming spectralComFreeVersion.py is in the same directory or accessible via PYTHONPATH
from spectralComFreeVersion import vectorize


class main:
    def dashBuild(self, statsDat_input_string):
        statsDatOut = {} # This will primarily hold robots.txt data from reconMata
        raw_html_content = "" # This will hold the HTML string for BeautifulSoup
        extracted_links = [] # This will hold links extracted by BeautifulSoup

        processed_statsDat = statsDat_input_string

        # Clean the protocol from the input URL
        if 'https://' in processed_statsDat:
            processed_statsDat = processed_statsDat.replace('https://', '')
        elif 'http://' in processed_statsDat:
            processed_statsDat = processed_statsDat.replace('http://', '')

        statsDat_parts = processed_statsDat.split(':', 1)

        buildDash = ""
        userTarget_raw = ""

        # Safely assign buildDash (e.g., "SCAN", "BUILD")
        if len(statsDat_parts) > 0:
            # Clean square brackets from the buildDash part (e.g., "[SCAN]")
            buildDash = statsDat_parts[0].replace('[','').replace(']','').strip()
        else:
            print(f"ERROR_INVALID_USAGE:Invalid input format. Expected at least one part for buildDash. Input: {statsDat_input_string}")
            sys.exit(1)

        # Safely assign userTarget_raw (the actual domain/URL)
        if len(statsDat_parts) > 1:
            userTarget_raw = statsDat_parts[1].replace(' ','').replace('[','').replace(']','').strip()
        else:
            # If no colon is found, assume the entire cleaned string is the target
            userTarget_raw = buildDash # The first part (after protocol removal) becomes the target
            buildDash = "DEFAULT_SCAN" # Provide a default operation type
            print(f"Warning: No explicit operation type found in input '{statsDat_input_string}'. Treating '{userTarget_raw}' as target and '{buildDash}' as operation type.")


        # Sanitize userTarget for valid directory names without 're'
        # Allowed characters for filesystem: alphanumeric, hyphen, underscore, dot
        allowed_chars_for_path = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_."
        userTarget_sanitized = "".join(c for c in userTarget_raw if c in allowed_chars_for_path).lower()

        if not userTarget_sanitized: # Fallback if sanitization results in an empty string
            userTarget_sanitized = "default_target"

        # Construct the full path for the target directory
        full_target_dir = os.path.join(os.getcwd(), userTarget_sanitized)

        # *** Directory creation using os.makedirs for robustness and proper error handling ***
        try:
            print(f"Attempting to create directory: {full_target_dir}")
            os.makedirs(full_target_dir, exist_ok=True)
            print(f"Directory '{full_target_dir}' ensured to exist.")
        except Exception as e:
            print(f"ERROR_GENERATING_PROFILE:Critical error creating directory '{full_target_dir}': {e}")
            sys.exit(1) # Exit with an error code

        # Fetch and process data using the vectorize class
        # spectralComFreeVersion.py's reconMata() is now expected to return (stats_data_dict, raw_html_string)
        try:
            temp_result = vectorize(userTarget_raw).shift0().reconMata()
            if isinstance(temp_result, tuple) and len(temp_result) == 2:
                statsDatOut, raw_html_content = temp_result
            else:
                print("Warning: spectralComFreeVersion.py did not return expected (dict, html_string) tuple.")
                statsDatOut = temp_result if isinstance(temp_result, dict) else {}
                raw_html_content = "" # Ensure raw_html_content is empty if not returned
        except Exception as e:
            print(f"ERROR_GENERATING_PROFILE:Failed to vectorize target '{userTarget_raw}' or get raw HTML: {e}")
            sys.exit(1)

        # Debug print: What did reconMata return?
        import json
        print("\n--- Debug: statsDatOut (Robots.txt data) from reconMata ---")
        try:
            print(json.dumps(statsDatOut, indent=2))
        except TypeError:
            print(statsDatOut)
        print("\n--- Debug: Raw HTML content (first 500 chars) ---")
        print(raw_html_content[:500] + ("..." if len(raw_html_content) > 500 else ""))
        print("-----------------------------------\n")

        # *** BeautifulSoup Link Extraction (Vectors) ***
        if raw_html_content:
            try:
                soup = BeautifulSoup(raw_html_content, 'html.parser')
                # Find all <a> tags and extract their 'href' attribute
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    extracted_links.append(href)
                print(f"Extracted {len(extracted_links)} links using BeautifulSoup.")
            except Exception as e:
                print(f"ERROR_PARSING_HTML:Failed to parse HTML or extract links with BeautifulSoup: {e}")
        else:
            print("Warning: No raw HTML content available for BeautifulSoup parsing to extract links.")


        # Consolidate all data (robots.txt and extracted links) into link0_data for HTML generation
        link0_data = []

        # Add data from statsDatOut (primarily robots.txt entries)
        if statsDatOut:
            for key, value in sorted(statsDatOut.items()):
                # Only include entries that are explicitly for robots.txt
                if str(key).startswith("ROBOTS-"):
                    link0_data.append(f"Disallowed Path: {value}")
                # Add other types of 'statsDatOut' data here if they are not links
                # For example, if reconMata also gives you "CVE-1234": "Description"
                # elif str(key).startswith("CVE-"):
                #     link0_data.append(f"Vulnerability ({key}): {value}")
        else:
            print("No robots.txt data from statsDatOut.")

        # Add extracted links to link0_data as "vectors"
        if extracted_links:
            for idx, link in enumerate(extracted_links):
                # Format links as vectors. Adding "PAID-SERVICE" as per your previous request.
                link0_data.append(f"Extracted Link {idx+1}: {link} PAID-SERVICE")
        else:
            print("No links extracted by BeautifulSoup to display as vectors.")


        # Generate the full HTML parts from link0_data
        link0 = ""
        if link0_data:
            link0 = "\n".join([f'''
                <div class="stat-box">
                    <p>{content}</p>
                </div>
            ''' for content in link0_data])
        else:
            print("No data (robots.txt or links) found to display in profile.html.")


        # Construct the full path for the output HTML file
        output_html_path = os.path.join(full_target_dir, 'profile.html')

        try:
            with open(output_html_path, 'w') as profile:
                # Decide which HTML template to write based on whether data was found
                if link0.strip() != '': # Check if link0 actually contains any content after stripping whitespace
                    profile.write(f'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Results for {userTarget_sanitized}</title>
                <link rel="stylesheet" href="/styles2.css">
            </head>
            <body>
                <!-- Header and Menu -->
                <header class="header">
                    <div class="logout-btn-container">
                    </div>
                    <div class="logo">
                        <img class="topBar" src="/images/backdrop.png" alt="Company Backdrop">
                    </div>
                    <nav class="nav">
                        <ul class="nav-links">
                            <li><a href="/demo">Vector Scan</a></li>
                            <li><a href="/mya">Project-MYA</a></li>
                            <li><a href="/database">Database</a></li>
                        </ul>
                    </nav>
                </header>

                <!-- Main Content Layout: Video Gallery + Dashboard -->
                <div class="main-content">
                    <!-- Dashboard Section -->
                    <div class="dashboard">
                        <h2>{buildDash[:6] if buildDash else "DATA"}:<br>{userTarget_sanitized} [⬇️]</h2>
                        <div class="stats-container" id='memoryLink0'>
                        {link0}
                        </div>
                    </div>
                    <script src='/scripts/inject.js'></script>
                </div>
            </body>
            <div class="copyrightNotice">
                <footer><p>Copyrights:<br> Rainai Inc. @2025</p></footer>
            </div>
            </html>
            ''')
                else: # This block for "No Results.gif" (if link0 is empty)
                    profile.write(f'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Results for {userTarget_sanitized}</title>
                <link rel="stylesheet" href="/styles2.css">
            </head>
            <body>
                <!-- Header and Menu -->
                <header class="header">
                    <div class="logout-btn-container">
                    </div>
                    <div class="logo">
                        <img class="topBar" src="/images/backdrop.png" alt="Company Backdrop">
                    </div>
                    <nav class="nav">
                        <ul class="nav-links">
                            <li><a href="/demo">Vector Scan</a></li>
                            <li><a href="/mya">Project-MYA</a></li>
                            <li><a href="/database">Database</a></li>
                        </ul>
                    </nav>
                </header>

                <!-- Main Content Layout: Video Gallery + Dashboard -->
                <div class="main-content">
                    <!-- Dashboard Section -->
                    <div class="dashboard">
                        <h2>{buildDash[:6] if buildDash else "DATA"}:<br>{userTarget_sanitized} [⬇️]</h2>
                        <div class="stats-container">
                        <img class="modern0" src='/images/No Results.gif'>
                        </div>
                    </div>
                </div>
            </body>
            <div class="copyrightNotice">
                <footer><p>Copyrights:<br> Rainai Inc. @2025</p></footer>
            </div>
            </html>
            ''')
            print(f"PROFILE_GENERATED:{userTarget_sanitized}/profile.html") # Success message for Node.js
            sleep(0.7) # Small delay, not strictly necessary for file write itself
        except Exception as e: # Catch any errors during file writing
            print(f"ERROR_GENERATING_PROFILE:Critical error writing profile.html to {output_html_path}: {e}")
            sys.exit(1) # Exit with an error code

# This block ensures dashBuild is called with the command-line argument when executed directly
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Create an instance of the main class and call its dashBuild method
        main_instance = main()
        main_instance.dashBuild(sys.argv[1])
    else:
        print("ERROR_INVALID_USAGE:Usage: python dashbuild.py \"[SCAN]: example.com\"")
        print("Example: python dashbuild.py \"[BUILD]: google.com:web_search\"")
        sys.exit(1) # Exit with an error code if no argument is provided
