# Ubuntu_Requests

### Python Libraries Assignment  
###  Description  

# 🖼️ Ubuntu-Inspired Image Fetcher Assignment  
## 🌍 The Wisdom of Ubuntu: "I am because we are"  

In the spirit of Ubuntu, which emphasizes community and sharing, your task is to create a program that connects to the global community of the internet, respectfully fetches shared resources, and organizes them for later appreciation.  

## 🎯 Your Task  
Create a Python script that:  
- Prompts the user for a URL containing an image  
- Creates a directory called `Fetched_Images` if it doesn't exist  
- Downloads the image from the provided URL  
- Saves it to the `Fetched_Images` directory with an appropriate filename  
- Handles errors gracefully, respecting that not all connections succeed  

### ⚙️ Requirements   
- Use the **requests** library to fetch the image  
- Check for HTTP errors and handle them appropriately  
- Create the directory if it doesn't exist using `os.makedirs()` with `exist_ok=True`  
- Extract the filename from the URL or generate one if not available  
- Save the image in binary mode  

### 💡 Ubuntu Principles to Implement  
- **Community** 🤝: Your program should connect to the wider web community  
- **Respect** 🙏: Handle errors gracefully without crashing  
- **Sharing** 📤: Organize the fetched images for later sharing  
- **Practicality** 🛠️: Create a tool that serves a real need  


💾 **Save Your Work** in a GitHub repo called `Ubuntu_Requests` and submit the URL for this repository to complete the assignment.  



## Example Output
**Terminal Output Text**  
```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.
```

## Starter Code Structure
python
```
import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:
            filename = "downloaded_image.jpg"
            
        # Save the image
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()
```

## ❓ Challenge Questions  
- Modify the program to handle multiple URLs at once.
- Implement precautions that you should take when downloading files from unknown sources.  
- Implement a feature that prevents downloading duplicate images.  
- Implement what HTTP headers might be important to check before saving the response content.  


## 🏆 Evaluation Criteria 
- ✅ Proper use of the **requests** library for fetching content  
- ⚠️ Effective error handling for network issues  
- 📂  Appropriate file management and directory creation  
- 📝 Clean, readable code with clear comments  
- 🤝 Faithfulness to **Ubuntu principles** of community and respect  


### 💭 Remember   
*"A person is a person through other persons."* – Ubuntu philosophy. Your program connects you to the work of others across the web.  
