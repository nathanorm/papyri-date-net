# ⚠️ Data Required

This directory is the designated location for all project data, but it is **intentionally left empty** in the repository.

You must provide the data yourself to run the project.

## 1. `data/images/`

This folder must be populated with all your papyrus images (e.g., `.jpg`, `.png`).

## 2. `data/metadata.csv`

This file is the **master list** that maps your images to their dates. You must create this file.

### Required Format

The file **must** be a CSV with two columns:

1.  `filename`: (string) The exact filename of the image in the `images/` folder.
2.  `date`: (integer/float) The date of the papyrus.

**Date Convention:**
* **AD/CE dates** are positive numbers (e.g., `50`).
* **BC/BCE dates** are negative numbers (e.g., `-150`).

### Example: `metadata.csv`

```csv
filename,date
papyrus_001.jpg,-150
papyrus_002.jpg,50
papyrus_003.jpg,-75
papyrus_004.jpg,25
```

Once you have added these files, you can proceed to `notebooks/00_data_exploration.ipynb` to split the data and begin the analysis.