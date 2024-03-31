import math
def calculate_circle_area(radius):
    return math.pi*radius**2
def calculate_tri_area(b,h):
    return 0.5*b*h
def main():
    radius=5
    a1=calculate_circle_area(5)
    base=6
    height=8
    a2=calculate_tri_area(base,height)
    print(a1,a2)
    
if __name__=="__main__":
    main()