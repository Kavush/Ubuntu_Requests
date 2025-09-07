# Ubuntu Image Fetcher

A Python tool for mindfully collecting images from the web, built with Ubuntu principles in mind: **Community, Respect, Sharing, and Practicality**.

## Features

- 📥 Download images from URLs with intelligent filename detection
- 🛡️ Safety precautions against malicious files and large downloads
- 🔍 Duplicate detection using content hashing
- 📁 Automatic directory creation and organization
- 🚦 Comprehensive error handling with user-friendly messages
- 🔄 Support for multiple URLs in a single operation

## Ubuntu Principles Implemented

### Community
- Connects to the wider web community to share and collect resources
- Uses respectful User-Agent headers to identify itself properly

### Respect
- Handles errors gracefully without crashing
- Respects server resources with proper timeout handling
- Provides clear feedback about operations

### Sharing
- Organizes downloaded images in a structured directory
- Prevents duplicate downloads to conserve resources
- Creates a tool that can be shared and used by others

### Practicality
- Solves a real-world need for image collection
- Easy to use with clear prompts and feedback
- Safe and reliable operation

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Kavush/Ubuntu_Requests.git
cd Ubuntu_Requests
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

Run the script:
```bash
python ubuntu_image_fetcher.py
```

Enter one or more image URLs when prompted (separate multiple URLs with commas).

Example:
```
Please enter image URLs (separate multiple URLs with commas): https://example.com/image1.jpg, https://example.com/image2.png
```

## Safety Features

- **URL Validation**: Ensures URLs use proper http/https protocols
- **Content-Type Checking**: Verifies responses are actually images
- **File Size Limits**: Prevents downloading files larger than 10MB
- **Safe Filenames**: Removes potentially harmful characters from filenames
- **Duplicate Prevention**: Uses MD5 hashing to avoid downloading the same image multiple times

## Project Structure

```
Ubuntu_Requests/
├── ubuntu_image_fetcher.py  # Main application
├── Fetched_Images/          # Directory for downloaded images
│   ├── .image_hashes.txt    # Hidden file for tracking duplicates
│   └── [downloaded images...]
└── README.md               # This file
```

## Code Overview

The application uses:
- `requests` library for HTTP operations
- `os` and `path` utilities for file management
- `hashlib` for duplicate detection
- `mimetypes` for proper file extension handling

Key functions:
- `main()`: Primary application workflow
- `is_duplicate_image()`: Checks for existing images using content hashing
- `save_image_hash()`: Stores image hashes to prevent future duplicates

## Error Handling

The tool gracefully handles:
- Network timeouts and connection errors
- Invalid URLs and non-image content
- Permission issues for file operations
- Large files that exceed safety limits

## Example Output

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Ubuntu Principles: Community, Respect, Sharing, Practicality
--------------------------------------------------
Please enter image URLs (separate multiple URLs with commas): https://example.com/ubuntu.jpg

Processing URL 1 of 1: https://example.com/ubuntu.jpg
  ✓ Successfully fetched: ubuntu.jpg
  ✓ Image saved to Fetched_Images/ubuntu.jpg

==================================================
Download Summary:
✓ Successful downloads: 1
⚠ Duplicates skipped: 0
✗ Errors encountered: 0

Connection strengthened. Community enriched.
```

## Contributing

This project embraces Ubuntu philosophy - contributions that improve community, respect, sharing, or practicality are welcome.

## License

This project is shared in the spirit of Ubuntu - for community benefit and learning.
