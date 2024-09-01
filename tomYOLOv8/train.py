import os
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
from ultralytics import YOLO

yaml = 'C:/Users/Lzd/Desktop/tomYOLOv8/ultralytics/cfg/models/v8/yolov8.yaml'

model = YOLO(yaml)

model.info()
if __name__ == "__main__":
    results = model.train(data='tomato.yaml',
                          name='yolov8',
                          epochs=200,
                          batch=10,device=0,workers=0)
