class Vehicle:
	def __init__(self,brand,name,price,colour):
		self.brand  = brand
		self.name   = name
		self.price  = price
		self.colour = colour
class TwoWheeler(Vehicle):
	def __init__(self,brand,name,price,colour,v_type,average,top_speed):
		Vehicle.__init__(self,brand,name,price,colour)
		self.v_type    = v_type
		self.average   = average
		self.top_speed = top_speed
class FourWheeler(TwoWheeler):
        def __init__(self,brand,name,price,colour,v_type,average,top_speed,v_class,v_capacity):
                TwoWheeler.__init__(self,brand,name,price,colour,v_type,average,top_speed)
                self.v_class    = v_class
		self.v_capacity = v_capacity



#v1= TwoWheeler("Honda","activa",75000,"white","Two Wheeler",45,80)
#v2= TwoWheeler("Suzuki","access",82000,"white","Two Wheeler",50,65)
#v3= FourWheeler("Hyundai","Creata",1225000,"black","Four Wheeler",12,180,"Suv",5)
#v4= FourWheeler("Tata","Nexon",1025000,"blue","Four wheeler",11,160,"suv",5)
#print("Welcome to vehicle buying guide")
#user_choice=int(input("Enter your budget for vehicle: "))
#if (user_choice <80000):
#	print ("you should buy activa \n The details are:\n Brand:{} \n name:{} \n price:{} \n colour:{} \n type:{} \n average:{} \n top speed:{}".format(v1.brand,v1.name,v1.price,v1.colour,v1.v_type,v1.average,v1.top_speed))
#elif (user_choice > 80000 and user_choice < 100000):
#	 print ("you should buy access \n The details are:\n Brand:{} \n name:{} \n price:{} \n colour:{} \n type:{} \n average:{} \n top speed:{}".format(v2.brand,v2.name,v2.price,v2.colour,v2.v_type,v2.average,v2.top_speed))
#elif (user_choice >100000 and user_choice < 1000000):
#	print ("there is no vehicle in the  range of (1lakh to 10 lakh) either increase aur decrease the price")
#elif (user_choice >1000000 and user_choice < 1200000):
#	 print ("you should buy nexon \n The details are:\n Brand:{} \n name:{} \n price:{} \n colour:{} \n type:{} \n average:{} \n top speed:{} \n class of vehicle: {} \n capacity of vehicle: {}".format(v4.brand,v4.name,v4.price,v4.colour,v4.v_type,v4.average,v4.top_speed,v4.v_class,v4.v_capacity))
#else:
#	 print ("you should buy creata \n The details are:\n Brand:{} \n name:{} \n price:{} \n colour:{} \n type:{} \n average:{} \n top speed:{}".format(v3.brand,v3.name,v3.price,v3.colour,v3.v_type,v3.average,v3.top_speed,v3.v_class,v3.v_capacity))

