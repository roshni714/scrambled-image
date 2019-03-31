import torch.nn as nn
import network

def main():
    device = torch.device(
        "cuda:0" if torch.cuda.is_available() and config["test"][
            "device"] == "cuda" else "cpu")

    # Build model architecture
        num_channels = 1
        model_name = "resnet18"
        im_size = 224
        num_classes = 1000
        model = network.network.get_model(name=model_name,
                                          pretrained=True,
                                          num_channels=num_channels,
                                          num_classes=num_classes)
        model.to(device)

    test_loader = get_data_loader(config)

    evaluate(model, test_loader, device)
