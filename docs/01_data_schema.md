# Data Directory Guide

This directory contains the datasets required for the PapyrusDateNet project.

## 1. `images/`

* **Purpose:** This folder must contain all raw papyrus images.
* **Format:** `.jpg`, `.png`, or other standard image formats.

## 2. `metadata.csv` (Master File)

* **Purpose:** This is the single source of truth, mapping every image to its ground-truth date.
* **Format:** A CSV file with two required columns: `filename` and `date`.
* **Column Details:**
    * `filename`: (string) The exact filename of the image in the `images/` folder (e.g., `papyrus_001.jpg`).
    * `date`: (integer) The year of the papyrus.
* **Date Convention:**
    * **AD/CE dates** are represented as positive integers (e.g., `50` for 50 AD).
    * **BC/BCE dates** are represented as negative integers (e.g., `-150` for 150 BC).

**Example `metadata.csv`:**
```

filename,date
papyrus\_001.jpg,-150
papyrus\_002.jpg,50
papyrus\_003.jpg,-75

```

## 3. `train.csv` / `val.csv` / `test.csv`

* **Purpose:** These are the data splits used by the notebooks for training, validation, and testing.
* **Generation:** **Do not create or edit these files manually.** They are generated automatically by running the `notebooks/00_data_exploration.ipynb` notebook.
* **Format:** They follow the exact same format as `metadata.csv`.
