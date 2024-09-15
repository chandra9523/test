class Cylinder:

    pi = 3.14
    def __init__(self,height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = self.pi*(self.radius)**2*self.height
        return vol

    def surface_area(self):
        sa = 2*self.pi*self.radius*self.height + 2*self.pi*self.radius**2
        return sa
    
cl = Cylinder(2,3)

vol_of_cylinder = cl.volume()
print(vol_of_cylinder)

surf_area_cyln = cl.surface_area()

print(surf_area_cyln)

