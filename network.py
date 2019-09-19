import torch.nn as nn
from torchvision import models

def get_model(name, pretrained):
    """
    Method that returns a torchvision model given a model
    name, pretrained (or not), number of channels,
    and number of outputs
    Inputs:
        name - string corresponding to model name
        pretrained- Boolean for whether a pretrained
                    model is requested
        num_channels- int number of channels
        num_classes- number of outputs of the network
    """
    function = getattr(models, name)
    model = function(pretrained=pretrained)
    return model

