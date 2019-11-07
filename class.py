class Laptop:
	count=0
	def __init__(self,brand,name,price):
		Laptop.count +=1
		self.brand= brand
		self.name= name
		self.price = price
	def discount(self,dis):
		if(dis <50):
			d=(self.price/100)*dis
			return self.price - d
		else:
			print("discount not allowed")
		return self.price 
l1= Laptop("HP","1234",22000)
l2= Laptop("Dell","123sdc4",24000)
l3= Laptop("Asus","123sccd4",25000)
l4= Laptop("Lenovo","12dwdw34",202000)
l5= Laptop("Htc","12ddw4",2200)

dis=int(input("Enter the discount percentage:"))
print(l1.brand)
print("price after discount is :" + str(l1.discount(dis)))
print("total number of product are " + str(Laptop.count))

