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
    > **Note:** The `requirements.txt` file installs PyTorch. For the fastest performance on your specific machine, you may want to install PyTorch manually by following the [official instructions](https://pytorch.org/get-started/locally/) (e.g., selecting the correct CUDA version for your Windows PC).

---

## 💻 Hardware Requirements

This project is configured to run on different types of hardware. The code will automatically detect and use the best available device:

1.  **NVIDIA GPU (CUDA):** **Strongly recommended.** This is the fastest and most stable option for training. Your Windows PC with an NVIDIA GPU will use this.
2.  **Apple Silicon (MPS):** **Good for development.** Your MacBook (M1/M2/M3, etc.) will use this. It is significantly faster than a CPU but may be slower than a dedicated NVIDIA GPU.
3.  **CPU:** **Not recommended for training.** This is a fallback and will be extremely slow.

When you run the training or evaluation notebooks, the first cell output will confirm which device is being used.

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