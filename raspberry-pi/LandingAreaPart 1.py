def triangle_area( x1y1, x2y2, x3y3):
    try:
		### tels code to request info 
        x1y1= x1y1.split (',')
        x2y2= x2y2.split (',')
        x3y3= x3y3.split (',')

		#pull strings into floats 
        x1 =float(x1y1[0])
        y1 =float(x1y1[1])
        x2 =float(x2y2[0])
        y2 =float(x2y2[1])
        x3 =float(x3y3[0])
        y3 =float(x3y3[1])

		### couculates the area of object 
        area=abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)

        return area 

    except:
		### Tells code if not good return to point of origin 
            print("Point no good")
            area = 0 
			
            return area 

while True: 
    ### makes me request input from the user 
        Val1 = input("Enter the first cordinate in format x,y:    ")
        Val2 = input("Enter the second cordinate in format x,y:   ")
        Val3 = input("Enter the third cordinate in format x,y:    ")
        area = triangle_area(Val1, Val2, Val3)
        if area == 0:
            continue
        else:
            print(f"({Val1}) this is cordinate 1 ({Val2}) this is cordinate 2 ({Val3}) this is cordinate 3 ({area}) area")
	