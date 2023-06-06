import cv2
import numpy as np
import torch
import matplotlib as plt

onnx_model_path = "support/SimpleFruitsv1iyolov5pytorch-simplified.onnx"


net = cv2.dnn.readNetFromONNX(onnx_model_path)

# define a video capture object
vid = cv2.VideoCapture(0)

model = torch.hub.load('ultralytics/yolov5', 'custom', path='support/SimpleFruitsv1iyolov5pytorch.pt',
                       force_reload=True)
while (True):
    # Capture the video frame
    # by frame
    ret, image = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', image)

    results = model(image)
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.imshow(results.render()[0])
    plt.show()

    !python
    detect.py - -weights
    runs / train / {RES_DIR} / weights / best.pt \
    - -source
    {data_path} - -name
    {INFER_DIR}


    '''
    image = torch.from_numpy(image) / 255.0
    image = image.unsqueeze(0)
    image = torch.permute(image, (0, 3, 1, 2))
    pred = model(image)
    pred = non_max_suppression(pred)
    #bboxes = pred.xyxy
    print(pred)
    '''

    '''
    #image = cv2.imread(sample_image)
    blob = cv2.dnn.blobFromImage(image, 1.0 / 255, (224, 224), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    preds = net.forward()
    biggest_pred_index = np.array(preds)[0].argmax()
    print("Predicted class:", biggest_pred_index)
    labels = ['apple', 'bannana', 'orage']

    print("The class", biggest_pred_index, "corresponds to", labels[biggest_pred_index])

    '''
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

