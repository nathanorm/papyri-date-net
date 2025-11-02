import torch
import torch.nn as nn
from torchvision import models

def create_resnet_regressor(pretrained=True):
    """
    Loads a pre-trained ResNet model and replaces the final
    fully-connected layer for a regression task.
    """
    # Load a pre-trained model
    model = models.resnet50(pretrained=pretrained)

    # (Optional) Freeze all layers except the final one for faster fine-tuning
    # for param in model.parameters():
    #     param.requires_grad = False

    # Get the number of input features for the final layer
    num_ftrs = model.fc.in_features

    # Replace the final layer
    # We output 1 continuous value (the date)
    model.fc = nn.Linear(num_ftrs, 1)

    return model
