# See: https://github.com/ggambetta/computer-graphics-from-scratch
#
# import os
# os.system("pip install --ignore-installed  git+https://github.com/williamedwardhahn/DeepZoo")
from DeepZoo import *
init()
h = 256
w = 256
display = setup(256,256)
img = np.zeros((h,w,3))

# Scene setup.
viewport_size = 1
projection_plane_z = 1
camera_position = [0, 0, 0]
background_color = [255, 245, 255]
infty = float('inf')
null = None

class Sphere:
  def __init__(self, center, radius, color):
    self.center = center
    self.radius = radius
    self.color = color

spheres = [Sphere([0, -1, 3], 1, [0, 128, 80]),Sphere([2, 0, 4], 1, [0, 0, 255]),Sphere([-2, 0, 4], 1, [0, 255, 0])]


def DotProduct(v1,v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    
def Subtract(v1,v2):
    return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]


# Converts 2D canvas coordinates to 3D viewport coordinates.
def CanvasToViewport(p2d):
  return [p2d[0] * viewport_size / w, p2d[1] * viewport_size / h, projection_plane_z]


#  Computes the intersection of a ray and a sphere. Returns the values of t for the intersections.
def IntersectRaySphere(origin,direction,sphere):
    
    oc = Subtract(origin, sphere.center);
    k1 = DotProduct(direction, direction);
    k2 = 2*DotProduct(oc, direction);
    k3 = DotProduct(oc, oc) - sphere.radius*sphere.radius;

    discriminant = k2*k2 - 4*k1*k3
    if (discriminant < 0):
        return [infty, infty]
        
    t1 = (-k2 + np.sqrt(discriminant)) / (2*k1);
    t2 = (-k2 - np.sqrt(discriminant)) / (2*k1);
    return [t1, t2]
    
# Traces a ray against the set of spheres in the scene.
def TraceRay(origin, direction, min_t, max_t):
    closest_t = infty
    closest_sphere = null
    
    for i in range(len(spheres)):
        ts = IntersectRaySphere(origin, direction, spheres[i])
        if (ts[0] < closest_t and min_t < ts[0] and ts[0] < max_t):
            closest_t = ts[0]
            closest_sphere = spheres[i]
        if (ts[1] < closest_t and min_t < ts[1] and ts[1] < max_t):
            closest_t = ts[1]
            closest_sphere = spheres[i]
    
    if (closest_sphere == null):
        return background_color
     
    return closest_sphere.color;

while True:

    for x in range(-w//2+1,w//2-1):
        for y in range(-h//2+1,h//2-1):
            direction = CanvasToViewport([x,y])
            color = TraceRay(camera_position, direction, 1, infty)
            img[w//2+x,h//2-y] = color #256*np.random.random((1,1,3))#


    blit(display, img)

quit()
