# PapyrusDateNet

A project to predict the date of ancient papyri from images using deep learning.

##  Goals

...

## Installation & Setup

1.  Clone the repository:
    ```bash
    git clone git@github.com:NathOrmond/papyri-date-net.git
    cd papyri-date-net
    ```
2.  Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

##  How to Run

1.  Place data in the `data/images/` folder.
2.  Create `data/metadata.csv`.
3.  Run the `notebooks/00_data_exploration.ipynb` to split the data.
4.  Run the `notebooks/02_model_training.ipynb` to train the model.

## Project Structure

```
papyri-date-net/
├── data/           # Raw data and CSVs
├── notebooks/      # Experimental notebooks
├── src/            # Reusable Python source code
├── checkpoints/    # Saved model files
├── results/        # Generated plots and predictions
└── docs/           # Detailed documentation
```


## Data Setup

**This repository does not include the data YET.** 

1.  Add all your papyrus images to the `data/images/` directory.
2.  Create a `data/metadata.csv` file that lists your images and their corresponding dates.

For the exact format required, please see the detailed instructions in `data/README.md`.