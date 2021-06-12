#Solution to calculate the number of cans required to paint the wall
def paint_calc(height, width):
    area = float(height*width)
    return area/5

a=paint_calc(5, 5)
print(f"Number of cans required is {a} square meters")