import os
import re

def find_css_files(directory):
    """
    Recursively finds all CSS files in a directory and its subdirectories.
    """
    css_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.css'):
                css_files.append(os.path.join(root, file))
    return css_files

def extract_font_links(css_file):
    """
    Extracts font file links from a CSS file.
    """
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regular expression to match font file URLs
    font_url_pattern = r'url\((.*?)\)'
    font_urls = re.findall(font_url_pattern, content)

    font_files = []
    for url in font_urls:
        # Check if the URL contains any of the specified font file extensions
        if any(ext in url for ext in ['.woff', '.woff2', '.eot', '.ttf', '.svg']):
            font_files.append(url)

    return font_files

def main():
    # Get the current working directory
    current_dir = os.getcwd()

    # Find all CSS files in the current directory and its subdirectories
    css_files = find_css_files(current_dir)

    # List to store all font URLs
    all_font_links = []

    # Loop through the list of CSS files
    for css_file in css_files:
        font_links = extract_font_links(css_file)
        if font_links:
            all_font_links.extend(font_links)

    # Write font URLs to fonts.txt
    with open('fonts_files.txt', 'w', encoding='utf-8') as outfile:
        for link in all_font_links:
            outfile.write(link + '\n')

    print("Font URLs written to fonts.txt.")

if __name__ == "__main__":
    main()
