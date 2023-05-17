from ultralytics import YOLO

# Instantiate YOLO, and provide it with the data.yaml file from the annotated dataset downloaded from roboflow.com
yolo = YOLO()
# You need to replace this location with the location of your dataset's data.yaml
yolo.train(data='<location of data.yaml here!>', epochs=100)
yolo.export()

# After exporting you'll need to find the generated files, and within them you should find a file called best.pt
# The general location of this file is "runs/detect/train/weights/best.pt". That is what you will use in the
# yolo_xxxxxx.py file relavent to the dataset (Aim Lab or aimtrainer.io)