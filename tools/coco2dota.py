from pycocotools.coco import COCO
import json
import os

annFile = "/home/qilei/DATASETS/trans_drone/annotations/test_mix.json"
coco = COCO(annFile)

imgIds = coco.getImgIds()

save_folder_dir = "/home/qilei/DATASETS/trans_drone/annotations"

for imgId in imgIds:
    print(imgId)
    img = coco.loadImgs(imgId)[0]
    print(img['file_name'])
    save_dir = os.path.join(save_folder_dir,"labelTxt",img['file_name'].replace("jpg","txt"))
    file_holder = open(save_dir,'w')
    annIds = coco.getAnnIds(imgId)
    anns = coco.loadAnns(annIds)

    for ann in anns:
        print(ann)