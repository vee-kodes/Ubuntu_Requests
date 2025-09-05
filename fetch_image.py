# Challenge Questions
    # 1. Modify the program to handle multiple URLs at once.
    # 2. Implement precautions that you should  take when downloading files from unknown sources.
    # 3. Implement a feature that prevents downloading duplicate images.
    # 4. Implement what HTTP headers might be important to check before saving the response content.

import requests
import os
from urllib.parse import urlparse
    
def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # 2a. Implement precautions that you should  take when downloading files from unknown sources.
    # Allow only HTTP and HTTPS URLs.
    def safe_url(url):
        parsed = urlparse(url)
        return parsed.scheme in ["http", "https"]

    # 1. Modify the program to handle multiple URLs at once.
    # Get URLs from user
    print("Paste one image link at a time and press Enter.")
    print("When you are done, just press Enter on an empty line.\n")

    urls = []
    while True:
        url = input("Image URL: ").strip()
        if not url:  # Stop if input is blank
            break
        urls.append(url)

    if not urls:  # nothing was entered
        print("\nNo URLs were provided.")
    else:
        print("\nYou entered the following URLs:")
        for u in urls:
            print("-", u)

    # Fetch each url
    for url in urls:
        try:
            # 2b. Implement precautions that you should  take when downloading files from unknown sources.
            # Ensure URL is safe
            if not safe_url(url):
                print(f"✗ Skipping unsafe URL: {url}")
                continue

            # Create directory to store images if it doesn't exist
            os.makedirs("Fetched_Images", exist_ok=True)
          
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

            # 4. Implement what HTTP headers might be important to check before saving the response content.
            content_type = response.headers.get("Content-Type", "")
            if "image" not in content_type.lower():
                print(f"✗ Not an image: {url} (Content-Type: {content_type})")
                continue

            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > 10 * 1024 * 1024:  # >10 MB
                print(f"✗ Skipping {url}, file too large (>10 MB)")
                continue
            
            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
        
            if not filename:
                filename = "downloaded_image.jpg"
                
            # Save the image
            filepath = os.path.join("Fetched_Images", filename)

            # 3. Implement a feature that prevents downloading duplicate images.
            # Keep track of already downloaded filenames
            downloaded_files = set()

            if filename in downloaded_files or os.path.exists(filepath):
                print(f"⚠ Duplicate found, skipping: {filename}")
                continue

            # Save the file if it's not a duplicate and headers passed checks          
            with open(filepath, 'wb') as f:
                f.write(response.content)


            # Mark file(s) as fetched and downloaded   
            print(f"\n✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            print("\nConnection strengthened. Community enriched.\n")
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()