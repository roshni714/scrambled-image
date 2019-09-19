from class_label_to_human_readable import CLASS_TO_HUMAN_READABLE
from class_to_label import CLASS_TO_LABEL

def make_imagenet_sysnet_dictionary(sysnet_file):

    dic = {}
    with open(sysnet_file) as f:
        lines = f.readlines()[:-1]
    for line in lines:
        items= line.strip().replace(",", "").replace("'", "").split("\t")
        words =  items[1].split(" ")
        final_name = "_".join(words)
        dic[final_name] =items[0] 

    return dic

def make_imagenet_label_dictionary():

    dic = {}
    for i in CLASS_TO_HUMAN_READABLE:
        items = CLASS_TO_HUMAN_READABLE[i].replace(",", "").replace("'", "")
        words =  items.split(" ")
        final_name = "_".join(words)
        dic[i] = final_name 

    return dic

def make_imagenet_label_to_class_dictionary():
    dic = {}
    for i in CLASS_TO_LABEL:
        dic[CLASS_TO_LABEL[i]] = i
    return dic
    
print(make_imagenet_label_to_class_dictionary())
