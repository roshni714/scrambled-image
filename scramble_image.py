import cv2
import numpy as np

def create_scrambled_image(original, r):
    img = cv2.imread(original)

    img_name = original.split("/")[1]
    path_to_scrambled = 'scrambled/r_{}/{}'.format(r, img_name)

    newimg = cv2.resize(img, (224,224))

    origins = get_block_origins(r)
    assert len(origins) == r**2

    permutation = np.random.permutation(r**2)
    scrambled_img = np.zeros([224, 244, 3])

    pix_x= 0
    pix_y= 0
    
    for i in range(len(origins)):
        start_x, start_y = origins[i]
        block_origin_x, block_origin_y = origins[permutation[i]]
        block_length = int(224/r)
        for i in range(block_length):
            for j in range(block_length):
                if block_origin_x + i < 224 and block_origin_y + j < 224:
                    scrambled_img[start_x + i, start_y + j] = img[block_origin_x + i, block_origin_y + j]
                    print(start_x + i, start_y + j)
    cv2.imwrite(path_to_scrambled, scrambled_img)

def get_block_origins(r):
    """
    Method that returns the upper left corner of the blocks
    given a scrambling factor r.
    """
    block_length = int(224/r)
    origins = []
    x = 0
    y = 0
    for i in range(r):
        for j in range(r):
            origins.append((x + i * block_length, y + j * block_length))
    return origins

for r in range(1, 7):
    create_scrambled_image('content/goldfish-img0.png', r)
