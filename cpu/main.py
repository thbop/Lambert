import pygame
import pygame.gfxdraw
from pygame.math import Vector2, Vector3
import math


from time import time


pygame.init()

class Sphere:
    def __init__(self, pos: Vector3, radius: int):
        self.pos = pos
        self.r = radius**2

wsize = (1200, 800)
res = 5
size = (
    round(wsize[0] / res),
    round(wsize[1] / res)
)
window = pygame.display.set_mode(wsize)
screen = pygame.Surface(size)

def get_hit(x, y, s):
    hit = 0
    for z in range(100):
        if (x - s.pos.x)**2 + (y - s.pos.y)**2 + (z - s.pos.z)**2 < s.r and not hit:
            hit = z
    return Vector3(x, y, hit)

def get_normal(vec, s):
    return (s.pos - vec).normalize()

def to_color(v):
    return min(max(round(v * 255), 0), 255)

def uvec_to_color(vec):
    return (
        to_color(vec.x),
        to_color(vec.y),
        to_color(vec.z)
    )

def lambertian(normal: Vector3, light: Vector3):
    return normal.dot(light.normalize())

def render(spheres):
    for x in range(size[0]):
        for y in range(size[1]):
            for s in spheres:
                hitpoint = get_hit(x, y, s)
                if hitpoint.z != 0:
                    normal = get_normal(hitpoint, s)
                    v = to_color(lambertian(normal, Vector3(.5, 1, .5)))
                    pygame.gfxdraw.pixel(screen, x, y, (v, v, v))


clock = pygame.time.Clock()
running = True
screen.fill((0, 0, 0))

spheres = [
    Sphere(Vector3(120, 80, 50), 64),
]

start = time()
render(spheres)
window.blit(
    pygame.transform.scale(screen, wsize),
    (0, 0)
)
pygame.display.flip()
print('Done!\nTime: ' + str( time() - start ))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(60)
    