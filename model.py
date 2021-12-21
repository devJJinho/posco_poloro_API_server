
class wareHouse:
    def __init__(self,init=None):
        if init !=None:
            self.index={
                'A':0,
                'B':1,
                'C':2,
                'X':3
            }
            self.status=[0 for x in range(len(self.index))]
            self.map=[
                [0,1,0,0], # A
                [1,0,1,0], # B
                [0,1,0,1], # C
                [0,0,1,0]  # X
                #A B C X 
            ]

    def setDensity(self,area,degree):
        self.status[self.index[area]]=degree
    
    def getDensity(self,area):
        return self.status[self.index[area]]

    def getPath(self,origin,dest):
        # Need algorithm
        pass
    
    def getMap(self):
        return self.map

class carStatus:
    def __init__(self,num):
        self.reset_data={"index":None,"status":False,"destPoint":None,"prePoint":None}
        self.status=[{"index":x,"status":False,"destPoint":None,"prePoint":None}.copy() for x in range(num)]
    
    def call(self,index,destination):
        self.status[index]['index']=index
        self.status[index]['status']=True
        self.status[index]['destPoint']=destination
    
    def update(self,index,status,destPoint,prePoint):
        self.status[index]['index']=index
        self.status[index]['status']=status
        self.status[index]['destPoint']=destPoint
        self.status[index]['prePoint']=prePoint
    
    def getStatus(self,index):
        return self.status[index]

    def getCarNum(self):
        return len(self.status)

    def reset(self,index):
        self.status[index]['status']=self.reset_data['status']
        self.status[index]['destPoint']=self.reset_data['destPoint']
        self.status[index]['prePoint']=self.reset_data['prePoint']
