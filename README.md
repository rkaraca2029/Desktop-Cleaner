# Downloads Folder Organizer

A Python script that automatically organizes files in your Downloads folder by sorting them into subfolders based on their file type.

## Features

- Automatically detects file types based on extensions
- Creates organized subfolders (Images, Documents, Videos, Music, Archives, Executables, Code, Others)
- Moves files from the root Downloads folder into appropriate categories
- Safe operation - only moves files, doesn't delete anything

## Requirements

- Python 3.x
- macOS (the script uses `~/Downloads` path)

## Usage

1. Clone or download this repository
2. Run the script:

```bash
python main.py
```

Or make it executable and run directly:

```bash
chmod +x main.py
./main.py
```

## File Categories

The script organizes files into the following categories:

- **Images**: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg, .webp
- **Documents**: .pdf, .doc, .docx, .txt, .rtf, .odt, .xls, .xlsx, .ppt, .pptx
- **Videos**: .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm
- **Music**: .mp3, .wav, .flac, .aac, .ogg, .wma
- **Archives**: .zip, .rar, .7z, .tar, .gz, .bz2
- **Executables**: .exe, .msi, .dmg, .pkg, .deb, .rpm
- **Code**: .py, .js, .html, .css, .java, .cpp, .c, .php, .rb
- **Others**: Any files with unrecognized extensions

## Notes

- The script only processes files in the root of the Downloads folder
- Existing subfolders are not processed (to avoid reorganizing already organized files)
- Files without extensions go into the "Others" folder
- The script will create category folders as needed

## Safety

- The script only moves files, it never deletes them
- Test the script on a small set of files first if you're concerned
- The script will print what it's doing, so you can monitor the process
