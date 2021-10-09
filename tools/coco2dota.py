from pycocotools.coco import COCO
import json
import os

annFile = "/home/qilei/DATASETS/trans_drone/annotations/test_mix.json"
coco = COCO(annFile)

imgIds = coco.getImgIds()

catIds = coco.getCatIds()

coco.loadCats()

save_folder_dir = "/home/qilei/DATASETS/trans_drone/"

for imgId in imgIds:
    img = coco.loadImgs(imgId)[0]
    save_dir = os.path.join(save_folder_dir,"labelTxt",img['file_name'].replace("jpg","txt"))
    file_holder = open(save_dir,'w')
    annIds = coco.getAnnIds(imgId)
    anns = coco.loadAnns(annIds)

    for ann in anns:
        if len(ann['segmentation'][0])==8:
            line = ''
            for x_y in ann['segmentation'][0]:
                line+=str(x_y)
                line+=' '
            print(coco.loadCats(ann['category_id']))
            line+=coco.loadCats(ann['category_id'])[0]['name']
            line+=' '
            line+='0\n'
            file_holder.write(line)