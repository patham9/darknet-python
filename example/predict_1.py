import numpy
import time
from PIL import Image
from darknet.api2.predictor import get_YOLOv2_Predictor, get_YOLOv3_Predictor, get_YOLOv3_Tiny_Predictor

filename = "dog.jpg"
image = Image.open(filename)
img = numpy.array(image)

# this will take few seconds .. but we need to create predictor only once
# predictor = get_YOLOv2_Predictor() # OK
predictor = get_YOLOv3_Predictor() # OK
# predictor = get_YOLOv3_Tiny_Predictor() # OK

t = time.time()
lis = predictor(img)
print("Predicting took", time.time()-t, "seconds") # takes around 0.2 secs on a decent (5.1 grade) GPU
for l in lis:
    print(l)

filenames=["dog.jpg", "eagle.jpg", "giraffe.jpg", "horses.jpg", "kite.jpg", "person.jpg"]

for filename in filenames:
    image = Image.open(filename)
    img = numpy.array(image)
    t = time.time()
    lis = predictor(img)
    print("Predicting took", time.time()-t, "seconds") # takes around 0.2 secs on a decent (5.1 grade) GPU
    for l in lis:
        print(l)
