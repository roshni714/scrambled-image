import torch
import torch.nn as nn
import network
import data_loader
import torchvision.transforms as transforms
from class_to_label import CLASS_TO_LABEL
from label_to_class import LABEL_TO_CLASS

def get_data_loader():
    size = 224
    data_transforms = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    dataset = data_loader.MatchToSampleDataset(data_transforms)

    loader = torch.utils.data.DataLoader(dataset,
                                                   batch_size=1, shuffle=False)
    return loader

def evaluate(model, dataset, device):
    count = 0
    model.eval()

    accuracy = {"r_1": 0,
                "r_2": 0, 
                "r_3": 0, 
                "r_4": 0,
                "r_5": 0,
                "r_6": 0}


    for match_to_sample in dataset:
       for r in range(1, 7):
            outputs = {}
            im, label = match_to_sample[r]["Q"]
            im = im.to(device)
            output = model(im)

            a= output[0][LABEL_TO_CLASS[match_to_sample[r]["A"]]]
            ia1 = output[0][LABEL_TO_CLASS[match_to_sample[r]["IA1"]]]
            ia2 = output[0][LABEL_TO_CLASS[match_to_sample[r]["IA2"]]]
            ia3= output[0][LABEL_TO_CLASS[match_to_sample[r]["IA3"]]]

            prob_dist = torch.softmax(torch.Tensor([a, ia1, ia2, ia3]), 0)

            if torch.argmax(prob_dist) == 0:
                accuracy["r_{}".format(r)] += 1
       count +=1
    for r in accuracy:
        accuracy[r] /=count
    print(accuracy)
            
def main():
    device = torch.device(
        "cuda:0" if torch.cuda.is_available() else "cpu")

    # Build model architecture
    num_channels = 3
    model_name = "resnet152"
    im_size = 224
    num_classes = 1000
    model = network.get_model(name=model_name,
                                          pretrained=True)
    model.to(device)

    test_loader = get_data_loader()

    evaluate(model, test_loader, device)

main()
