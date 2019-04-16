

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

print(make_imagenet_sysnet_dictionary("sysnets.txt"))
