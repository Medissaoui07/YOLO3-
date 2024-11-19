import numpy  as  np 
import cv2 


class Yolo(): 

    def __init__(self , weights  , config , confidence_threshhold ,):

        self.net = cv2.dnn.readNetFromDarknet(config , weights)
        self.layers_name=self.net.getLayerNames()
        self.threshhold=confidence_threshhold




        


    def preprocess (self , image )  : 
        h,w=image.shape[:2]
        blob = cv2.dnn.blobFromImage(image , 1/255,crop=False ,size=(h,w))  



    def postprocess(self  ,  outputs ) : 
        
        for output in outputs : 
            print("postprocess function .... output shape : " , output.shape)
            for detection in output  : 
                print("postprocess function ....detection shape : " , detection.shape)
                
                box=detection[:4]
                confidence=detection[4]
                class_probabilities =detection[5:] 
               
                class_id=np.argmax(class_probabilities)
                class_score=class_probabilities[class_id]

                if class_score > self.threshhold : 

                    cx,cy,bw,bh= box*np.array()
                    




        



    def process(self,image): 
        blob = self.preprocess(image) 
        self.net.setInput(blob=blob)
        outputs=self.net.forward(self.layers_name)
        

    def iou(self): 
          
    def non_max_supression(self): 


    def draw_boxes(self):