from flask import Flask,request
import pandas as pd
import pickle
from math import exp
app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def adder_page():
	if request.method=="POST":
    	year=int(request.form["year"])
    	manufacturer=request.form["manufacturer"]
    	condition=request.form["condition"]
    	cylinders=int(request.form["cylinders"])
    	fuel=request.form["fuel"]
    	odometer=int(request.form["odometer"])
    	title_status=request.form["title_status"]
    	transmission=request.form["transmission"]
    	drive=request.form["drive"]
    	vtype=request.form["vtype"]
    	paint_color=request.form["paint_color"]
    	state=request.form["state"]
    	test_data={"year":[year],"manufacturer":[manufacturer],"condition":[condition],"cylinders":[cylinders],
           	"fuel":[fuel],"odometer":[odometer],"title_status":[title_status],"transmission":[transmission],
           	"drive":[drive],"type":[vtype],"paint_color":[paint_color],"state":[state]}
    	test=pd.DataFrame(test_data)
    	test["year"]=((test["year"]-1900)/(2020-1900))
    	test["odometer"]=((test["odometer"]-0)/(10000000-0))
    	test["cylinders"]=((test["cylinders"]-0)/(6-0))
    	regressor=pickle.load(open('/home/ajithkumar/Desktop/TestPrice/RandomFReg.pkl','rb'))
    	xx_columns=pickle.load(open('/home/ajithkumar/Desktop/TestPrice/xx_columns.pkl','rb'))
    	testmodel=pd.get_dummies(test)
    	missing_cols=set(xx_columns)-set(testmodel.columns)
    	for val in missing_cols:
        	testmodel[val]=0
    	testmodel=testmodel[xx_columns]
    	result=regressor.predict(testmodel)
    	result=exp(result)-1
    	return '''
       	<html>
           	<body>
           	<p>Price in $ {result}</p>
           	</body>
       	</html>
   	'''.format(result=result)
    
	return '''
    	<html><head></head><body>
	<h3>Price Prediction</h3>
<div>
<form action"." method="POST">
Model Year: <input name="year" type="text"> <br>
Manufacturer:<select name="manufacturer">
<option value="ford">Ford</option>
<option value="chevrolet">Chevrolet</option>
<option value="toyota">Toyota</option>
<option value="nissan">Nissan</option>
<option value="ram">Ram</option>
<option value="honda">Honda</option>
<option value="jeep">Jeep</option>
<option value="gmc">GMC</option>
<option value="dodge">Dodge</option>
<option value="bmw">BMW</option>
<option value="hyundai">Hyundai</option>
<option value="mercedes-benz">Mercedes-Benz</option>
<option value="subaru">Subaru</option>
<option value="volkswagen">Volkswagen</option>
<option value="kia">Kia</option>
<option value="chrysler">Chrysler</option>
<option value="cadillac">Cadillac</option>
<option value="lexus">Lexus</option>
<option value="buick">Buick</option>
<option value="mazda">Mazda</option>
<option value="audi">Audi</option>
<option value="acura">Acura</option>
<option value="infiniti">Infiniti</option>
<option value="lincoln">Lincoln</option>
<option value="pontiac">Pontiac</option>
<option value="volvo">Volvo</option>
<option value="mitsubishi">Mitsubishi</option>
<option value="mini">Mini</option>
<option value="rover">Rover</option>
<option value="mercury">Mercury</option>
<option value="saturn">Saturn</option>
<option value="jaguar">Jaguar</option>
<option value="fiat">Fiat</option>
<option value="harley-davidson">Harley-Davidson</option>
<option value="alfa-romeo">Alph-Romeo</option>
<option value="datsun">Datsun</option>
<option value="tesla">Tesla</option>
<option value="land rover">Land Rover</option>
<option value="porche">Porche</option>
<option value="aston-martin">Aston-Martin</option>
<option value="ferrari">Ferrari</option>
<option value="morgan">Morgan</option>
<option value="unknown">Unknown</option>
</select><br> Condition:<select name="condition">
<option value="new">New</option>
<option value="excellent">Excellent</option>
<option value="like new">Like New</option>
<option value="good">Good</option>
<option value="salvage">Salvage</option>
<option value="fair">Fair</option>
</select><br> Cylinders:<select name="cylinders">
<option value="0">3 cylinders</option>
<option value="1">4 cylinders</option>
<option value="2">5 cylinders</option>
<option value="3">6 cylinders</option>
<option value="4">8 cylinders</option>
<option value="5">10 cylinders</option>
<option value="6">12 cylinders</option>
</select><br> Fuel:<select name="fuel">
<option value="gas">Gas</option>
<option value="diesel">Diesel</option>
<option value="hybrid">Hybrid</option>
<option value="electric">Electric</option>
<option value="other">Other</option>
</select><br> Odometer: <input name="odometer" type="text"> <br> Title Status:<select name="title_status">
<option value="clean">Clean</option>
<option value="rebuilt">Rebuilt</option>
<option value="salvage">Salvage</option>
</select><br> Transmission:<select name="transmission">
<option value="automatic">Automatic</option>
<option value="manual">Manual</option>
<option value="other">Other</option>
</select><br> Drive:<select name="drive">
<option value="1wd">1wd</option>
<option value="2wd">2wd</option>
<option value="3wd">3wd</option>
<option value="4wd">4wd</option>
<option value="5wd">5wd</option>
<option value="6wd">6wd</option>
<option value="7wd">7wd</option>
</select><br>
Type:<select name="vtype">
<option value="sedan">Sedan</option>
<option value="SUV">SUV</option>
<option value="truck">Truck</option>
<option value="pickup">Pickup</option>
<option value="van">Van</option>
<option value="coupe">Coupe</option>
<option value="hatchback">Hatchback</option>
<option value="wagon">Wagon</option>
<option value="convertible">Convertible</option>
<option value="bus">Bus</option>
<option value="mini-van">Mini-Van</option>
<option value="offroad">Offroad</option>
<option value="other">Other</option>
</select><br>
Paint Color:<select name="paint_color">
<option value="white">White</option>
<option value="black">Black</option>
<option value="silver">Silver</option>
<option value="blue">Blue</option>
<option value="red">Red</option>
<option value="grey">Grey</option>
<option value="green">Green</option>
<option value="brown">Brown</option>
<option value="yellow">Yellow</option>
<option value="orange">Orange</option>
<option value="purple">Purple</option>
<option value="custom">Custom</option>
</select><br> State:<select name="state">
<option value="midwest">MidWest</option>
<option value="south">South</option>
<option value="northeast">NorthEast</option>
<option value="west">West</option>
</select><br>

<input type="submit" value="Submit">
</form>
</div>
 
 </body></html>

	'''


if __name__ == '__main__':
	app.run()
