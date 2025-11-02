import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from PIL import Image

class PapyriDataset(Dataset):
    """Custom Dataset for loading papyrus images and their dates."""
    
    def __init__(self, csv_file, img_dir, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with filenames and dates.
            img_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied on a sample.
        """
        self.metadata = pd.read_csv(csv_file)
        self.img_dir = img_dir
        self.transform = transform

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, idx):
        # Get image path
        img_name = self.metadata.iloc[idx, 0]
        img_path = os.path.join(self.img_dir, img_name)
        
        # Load image and ensure it's RGB (for pre-trained models)
        image = Image.open(img_path).convert('RGB')

        # Get date and convert to a float tensor
        # We use float32 for regression targets
        date = self.metadata.iloc[idx, 1]
        date = torch.tensor([date], dtype=torch.float32)

        # Apply transforms
        if self.transform:
            image = self.transform(image)

        return image, date
