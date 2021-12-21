from flask import Flask,request 
from flask_restx import Namespace,Api, Resource,cors 
from model import wareHouse,carStatus
from  flask_cors import CORS, cross_origin

app = Flask(__name__)  
api = Api(app)  
CORS(app)
ns = Namespace('inventories', description="Inventory",
               decorators=[cors.crossdomain(origin="*")])
@cross_origin()
@api.route('/cars/<string:index>') 
class Car(Resource):
    def post(self,index): # call
        if index==None:
            return
        index=int(index)
        if index>=cs.getCarNum():
            return {"error":"out of range"}
        data=request.json
        if data==None:
            return {"error":"No such  a car"}
        if cs.getStatus(index)['status']==True:
            return {"msg":"{} has been already started ".format(index)}
        cs.call(index,data.get('destPoint'))
        return {"msg":"{} called".format(index)}

    def get(self,index): 
        if index==None:
            return
        index=int(index)
        if index>=cs.getCarNum():
            return {"error":"out of range"}

        return cs.getStatus(index)

    def put(self,index):
        if index==None:
            return
        index=int(index)
        if index>=cs.getCarNum():
            return {"error":"out of range"}
        data=request.json
        if data==None:
            return {"error":"No such  a car"}
        cs.update(data.get('index'),data.get('status'),data.get('destPoint'),data.get('prePoint'))
        return {"msg":"{} updated".format(index)}
    
    def delete(self,index):
        if index==None:
            return
        index=int(index)
        if index>=cs.getCarNum():
            return {"error":"out of range"}
        cs.reset(index)
        return {"msg":"{} reset".format(index)}
            

if __name__ == "__main__":
    wh=wareHouse()
    cs=carStatus(1)
    app.run(debug=True, host='141.223.140.53', port=9666)