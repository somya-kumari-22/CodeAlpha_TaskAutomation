# CodeAlpha Internship — Python Task 3: Task Automation with Python Scripts

## What This Does
Automates 3 small real-life repetitive tasks using Python:
1. **Move all `.jpg` files** from one folder to another
2. **Extract all email addresses** from a `.txt` file
3. **Scrape the title** of a fixed webpage and save it

## Libraries Required
```bash
pip install requests beautifulsoup4
```
(os, shutil, re are built-in — no install needed)

## Sample Output
```
============================================
  Task Automation — Python Scripts
  CodeAlpha Python Internship — Task 3
============================================

--- Task A: Move JPG Files ---
✅ Moved: photo1.jpg → moved_images/
✅ Moved: photo2.jpg → moved_images/
Total files moved: 2

--- Task B: Extract Emails from Text File ---
✅ Emails found in sample_emails.txt:
   1. alice@gmail.com
   2. bob@yahoo.com
   3. contact@codealpha.tech
Total emails extracted: 3
✅ Saved to extracted_emails.txt

--- Task C: Scrape Webpage Title ---
✅ Page Title: Example Domain
✅ Title saved to webpage_title.txt

============================================
All 3 automation tasks completed! ✅
============================================
```

## Key Concepts Used (as per task)
- ✅ os — file and folder operations
- ✅ shutil — moving files
- ✅ re — regex for email extraction
- ✅ requests — fetching webpage
- ✅ BeautifulSoup — HTML parsing
- ✅ File handling — reading and writing files

## Output Files Generated
| File | What it contains |
|---|---|
| `moved_images/` | Folder with moved .jpg files |
| `extracted_emails.txt` | All emails found in text file |
| `webpage_title.txt` | Scraped title of the webpage |
