from PIL import Image
import numpy as np
import random

def find_ends(img):
    img = np.array(img)
    start = (254, 0, 0)
    end = (0, 9, 254)
    Ys, Xs = np.where(np.all(img==start, axis=2))
    Ye, Xe = np.where(np.all(img==end, axis=2))
    return (Xs[0], Ys[0]), (Xe[0], Ye[0])

def search(start, end, img, pix):
    current = start
    array = np.array(img)
    path = []
    intersects = []
    while current != end:
        possible = [(current[0]-1, current[1]), (current[0]+1, current[1]),
                    (current[0], current[1]-1), (current[0], current[1]+1)]
        possible = [move for move in possible if pix[move] >= (200, 200, 200) or pix[move] == (0, 9, 254) and pix[move] != (255, 255, 0) and move != start]
        if len(possible) >= 2:
            if current not in intersects:
                intersects.append(current)
        if not possible:
            current = intersects.pop()
            path = path[:path.index(current)]
        else:
            current = random.choice(possible)
        path.append(current)
        array[current[1], current[0]] = (255, 255, 0)
    for p in path:
        array[p[1], p[0]] = (0, 255, 0)
    img = Image.fromarray(array)
    img.save('image.png')

im = Image.open("/Users/FoFa/Downloads/maze_solver/maze-3.png")
pix = im.load()
start, end = find_ends(im)
search(start, end, im, pix)

#i used a small scope
#to create a website i need to have it accept all different types of images
#whats OCR?
#breath first search
#sql database postgres jscript
#json database
# do sql challenge and submit it
