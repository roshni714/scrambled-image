import csv
import cv2
"""
with open("match_to_sample.csv") as f:
	lines = f.readlines()

with open("metadata.csv", "wb") as metadata:
	filewriter = csv.writer(metadata, delimiter = ",")
	filewriter.writerow(["stimulus", "ia1", "ia2", "ia3", "ca"])

	for i in range(len(lines)):
		val  = lines[i].rstrip()
		categories = val.split(",")
		lines[i] = categories

	question_num = 1
	for line in lines[1:]:
		for scrambling_factor in [1, 3, 5, 7, 10, 15]:
			question_path ="scrambled/r_{}/{}.png".format(scrambling_factor, line[0])
			ia1_path = "content/{}/img0.png".format(line[1])
			ia2_path = "content/{}/img0.png".format(line[2])
			ia3_path = "content/{}/img0.png".format(line[3])
			ca_path =  "content/{}/img1.png".format(line[0])

			filewriter.writerow([question_path, ia1_path, ia2_path, ia3_path, ca_path])

"""
with open("metadata.csv", "r") as f:
	lines = f.readlines()
	
	for i in range(len(lines)):
		val  = lines[i].rstrip()
		categories = val.split(",")
		lines[i] = categories


	for line in lines[1:]:
		for path in line:
		    try:
                        img = cv2.imread(path)
	                resized_img = cv2.resize(img, (224,224))
		        cv2.imwrite(path, resized_img)
		    except:
			print(path)

		
		 


