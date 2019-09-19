import torch
from torch.utils.data import Dataset
import pandas as pd
from PIL import Image
from skimage import io

class MatchToSampleDataset(Dataset):

    def __init__(self, image_transform):
        self.df = pd.read_csv("match_to_sample.csv")
        self.image_transform = image_transform

    def __getitem__(self, idx):
        solution = {}

        for r in range(1, 7):
            sample = self.df["Q"][idx]
            ia1 = self.df["IA1"][idx]
            ia2 = self.df["IA2"][idx]
            ia3 = self.df["IA3"][idx]

            Q= Image.fromarray(io.imread("scrambled/r_{}/{}.png".format(r, sample)))
            Q.show() 
            A= Image.fromarray(io.imread("content/{}/img1.png".format(sample)))
            IA1= Image.fromarray(io.imread("content/{}/img1.png".format(ia1)))
            IA2= Image.fromarray(io.imread("content/{}/img1.png".format(ia2)))
            IA3= Image.fromarray(io.imread("content/{}/img1.png".format(ia3)))
           
            res = {"Q": (Q, sample), "A": (A, sample), "IA1": (IA1, ia1), "IA2": (IA2, ia2), "IA3": (IA3, ia3)}

            for key in res:
                im, label = res[key] 
                im = self.image_transform(im)
                res[key] = (im, label)
            solution[r] = res
        return solution

    def __len__(self):
        return len(self.df) 
