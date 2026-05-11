#!/usr/bin/env python3
"""
Downloads Folder Organizer

This script organizes files in the Downloads folder by moving them into
subfolders based on their file type (extension).
"""

import os
import shutil

def organize_downloads():
    # Get the path to the Downloads folder
    downloads_path = os.path.expanduser("~/Downloads")

    # Check if Downloads folder exists
    if not os.path.exists(downloads_path):
        print("Downloads folder not found at:", downloads_path)
        return

    # Define file type categories and their extensions
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
        'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Executables': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb'],
        'Others': []  # Catch-all for unrecognized extensions
    }

    # Get all files in the Downloads folder
    files = [f for f in os.listdir(downloads_path) if os.path.isfile(os.path.join(downloads_path, f))]

    if not files:
        print("No files found in Downloads folder.")
        return

    print(f"Found {len(files)} files to organize...")

    # Organize each file
    for file in files:
        file_path = os.path.join(downloads_path, file)
        _, ext = os.path.splitext(file)
        ext = ext.lower()

        # Determine category
        category = 'Others'
        for cat, extensions in categories.items():
            if ext in extensions:
                category = cat
                break

        # Create category folder if it doesn't exist
        category_path = os.path.join(downloads_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created folder: {category}")

        # Move file to category folder
        dest_path = os.path.join(category_path, file)
        try:
            shutil.move(file_path, dest_path)
            print(f"Moved: {file} -> {category}/")
        except Exception as e:
            print(f"Error moving {file}: {e}")

    print("Organization complete!")

if __name__ == "__main__":
    organize_downloads()