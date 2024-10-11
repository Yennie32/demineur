import settings
 # function to calculate the % of height 
def height_prct(percentage):
    return (settings.HEIGHT / 100) * percentage

# print(height_prct(25))

 # function to calculate the % of width 
def width_prct(percentage):
    return (settings.WIDTH / 100) * percentage

print(width_prct(50))
