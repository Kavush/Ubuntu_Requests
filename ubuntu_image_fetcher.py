import requests
import os
import hashlib
from urllib.parse import urlparse
import mimetypes

def create_image_downloader():
    """
    Ubuntu Image Fetcher - A tool for mindfully collecting images from the web
    Implements Ubuntu principles: Community, Respect, Sharing, Practicality
    """
    
    def main():
        print("Welcome to the Ubuntu Image Fetcher")
        print("A tool for mindfully collecting images from the web\n")
        print("Ubuntu Principles: Community, Respect, Sharing, Practicality")
        print("-" * 50)
        
        # Get URLs from user
        urls_input = input("Please enter image URLs (separate multiple URLs with commas): ")
        urls = [url.strip() for url in urls_input.split(',') if url.strip()]
        
        if not urls:
            print("✗ No URLs provided. Operation cancelled.")
            return
        
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        print("✓ Fetched_Images directory ready\n")
        
        successful_downloads = 0
        duplicate_count = 0
        error_count = 0
        
        for i, url in enumerate(urls, 1):
            print(f"Processing URL {i} of {len(urls)}: {url}")
            
            try:
                # Validate URL format
                if not url.startswith(('http://', 'https://')):
                    print("  ✗ Invalid URL format. Must start with http:// or https://")
                    error_count += 1
                    continue
                
                # Fetch the image with safety headers
                headers = {
                    'User-Agent': 'UbuntuImageFetcher/1.0 (Community Tool)'
                }
                
                response = requests.get(url, headers=headers, timeout=15, stream=True)
                response.raise_for_status()  # Raise exception for bad status codes
                
                # Check HTTP headers for safety
                content_type = response.headers.get('content-type', '')
                content_length = response.headers.get('content-length', 0)
                
                if not content_type.startswith('image/'):
                    print(f"  ✗ URL does not point to an image (Content-Type: {content_type})")
                    error_count += 1
                    continue
                
                # Limit file size for safety (10MB max)
                if content_length and int(content_length) > 10 * 1024 * 1024:
                    print("  ✗ File too large (max 10MB allowed)")
                    error_count += 1
                    continue
                
                # Extract filename from URL or generate one
                parsed_url = urlparse(url)
                filename = os.path.basename(parsed_url.path)
                
                if not filename or '.' not in filename:
                    # Generate filename based on content type
                    extension = mimetypes.guess_extension(content_type) or '.jpg'
                    filename = f"downloaded_image_{i}{extension}"
                
                # Create safe filename
                safe_filename = "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_')).rstrip()
                filepath = os.path.join("Fetched_Images", safe_filename)
                
                # Check for duplicates using content hash
                image_content = response.content
                content_hash = hashlib.md5(image_content).hexdigest()
                
                if is_duplicate_image(content_hash):
                    print(f"  ⚠ Duplicate image detected. Skipping: {safe_filename}")
                    duplicate_count += 1
                    continue
                
                # Save the hash to prevent future duplicates
                save_image_hash(content_hash)
                
                # Save the image
                with open(filepath, 'wb') as f:
                    f.write(image_content)
                
                print(f"  ✓ Successfully fetched: {safe_filename}")
                print(f"  ✓ Image saved to {filepath}")
                successful_downloads += 1
                
            except requests.exceptions.RequestException as e:
                print(f"  ✗ Connection error: {e}")
                error_count += 1
            except Exception as e:
                print(f"  ✗ An error occurred: {e}")
                error_count += 1
            
            print()  # Empty line for readability
        
        # Summary
        print("=" * 50)
        print("Download Summary:")
        print(f"✓ Successful downloads: {successful_downloads}")
        print(f"⚠ Duplicates skipped: {duplicate_count}")
        print(f"✗ Errors encountered: {error_count}")
        
        if successful_downloads > 0:
            print("\nConnection strengthened. Community enriched.")
    
    def is_duplicate_image(content_hash):
        """Check if an image with this content hash has already been downloaded"""
        hash_file = os.path.join("Fetched_Images", ".image_hashes.txt")
        
        if not os.path.exists(hash_file):
            return False
        
        with open(hash_file, 'r') as f:
            existing_hashes = f.read().splitlines()
        
        return content_hash in existing_hashes
    
    def save_image_hash(content_hash):
        """Save the content hash to prevent future duplicates"""
        hash_file = os.path.join("Fetched_Images", ".image_hashes.txt")
        
        with open(hash_file, 'a') as f:
            f.write(content_hash + '\n')
    
    return main

if __name__ == "__main__":
    image_downloader = create_image_downloader()
    image_downloader()