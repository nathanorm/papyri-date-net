import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def split_data(csv_path='data/metadata.csv', output_dir='data/', test_size=0.15, val_size=0.15, random_state=42):
    """
    Splits the master metadata.csv into train, val, and test sets.
    """
    df = pd.read_csv(csv_path)
    
    # Split off test set
    train_val_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
    
    # Split remaining into train and validation
    # Adjust val_size relative to the remaining data
    val_size_adjusted = val_size / (1.0 - test_size)
    train_df, val_df = train_test_split(train_val_df, test_size=val_size_adjusted, random_state=random_state)
    
    # Save to CSV
    train_df.to_csv(f"{output_dir}/train.csv", index=False)
    val_df.to_csv(f"{output_dir}/val.csv", index=False)
    test_df.to_csv(f"{output_dir}/test.csv", index=False)
    
    print(f"Data split complete:")
    print(f" - Train: {len(train_df)} samples -> {output_dir}/train.csv")
    print(f" - Val:   {len(val_df)} samples -> {output_dir}/val.csv")
    print(f" - Test:  {len(test_df)} samples -> {output_dir}/test.csv")

def save_loss_plot(train_losses, val_losses, output_path='results/loss_curve.png'):
    """Saves a plot of training and validation loss."""
    plt.figure(figsize=(10, 5))
    plt.plot(train_losses, label='Training Loss')
    plt.plot(val_losses, label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss (MSE)')
    plt.legend()
    plt.grid(True)
    plt.savefig(output_path)
    print(f"Loss curve saved to {output_path}")

def save_predictions_plot(y_true, y_pred, output_path='results/predictions_scatter.png'):
    """Saves a scatter plot of actual vs. predicted dates."""
    plt.figure(figsize=(8, 8))
    plt.scatter(y_true, y_pred, alpha=0.5)
    
    # Add a 1:1 line
    lims = [min(min(y_true), min(y_pred)), max(max(y_true), max(y_pred))]
    plt.plot(lims, lims, 'r--', label='Perfect Prediction')
    
    plt.title('Actual vs. Predicted Date')
    plt.xlabel('Actual Date')
    plt.ylabel('Predicted Date')
    plt.legend()
    plt.grid(True)
    plt.savefig(output_path)
    print(f"Prediction scatter plot saved to {output_path}")
