# 📱 Mobile Phone Web Scraper (Unique.com.mm)

## 📌 Overview

This project is a **Python web scraping script** that extracts **mobile phone product information** from the *Unique Myanmar* website. It collects:

* Product Name
* Product Price
* Product Availability Status

The extracted data is automatically saved into an **Excel file** with the current date.

---

## 🛠️ Technologies & Libraries Used

* **Python 3**
* `requests` – for sending HTTP requests
* `BeautifulSoup (bs4)` – for parsing HTML content
* `pandas` – for data processing and Excel export
* `tqdm` – for progress tracking
* `datetime` – for timestamping output files
* `time` – for request control

---

## ⚙️ Features

* Automatically detects the **last page number** of product listings
* Scrapes data across **all pages**
* Extracts:

  * Product name
  * Product price (converted to integer)
  * Stock status (high / low / normal)
* Displays a **progress bar** during scraping
* Exports results to an **Excel (.xlsx) file**

---

## 📂 Output

The script generates an Excel file in the project directory:

```
Output YYYY-MM-DD.xlsx
```

### Example Columns:

| Product Name | Product Price | Product Status |
| ------------ | ------------- | -------------- |
| iPhone 14    | 2350000       | In Stock       |

---

## 🚀 How to Run the Script

### 1️⃣ Install Required Packages

```bash
pip install requests beautifulsoup4 pandas tqdm html5lib
```

### 2️⃣ Run the Script

```bash
python main.py
```

(Replace `main.py` with your script filename if different.)

---

## 📌 Notes & Limitations

* This script relies on the **current HTML structure** of the website. Changes to the site may require updates to selectors.
* Ensure you have **stable internet connectivity** while running the script.
* Use responsibly and respect the website’s **terms of service**.

---

## 🔮 Future Improvements

* Fix page iteration bug (currently scraping only the last page)
* Add request headers & error handling
* Implement logging instead of print statements
* Export data to CSV or database
* Add command-line arguments for flexibility

---

## 👤 Author

**Thin Thin**
Civil / Hydraulic Engineer
Python & Data Automation Enthusiast

---
