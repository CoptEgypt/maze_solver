from PIL import Image  
import numpy as np    
import random        

# Function to find the start and end points in the maze image
def find_ends(img):
    img = np.array(img)  # Convert the image to a NumPy array 
    start = (254, 0, 0)  
    end = (0, 9, 254)    
    
    # Find the coordinates of the start and end points in the image
    Ys, Xs = np.where(np.all(img==start, axis=2))
    Ye, Xe = np.where(np.all(img==end, axis=2))
    
    return (Xs[0], Ys[0]), (Xe[0], Ye[0])  # Return the coordinates of the start and end points

# Function to search for a path from the start to the end point in the maze
def search(start, end, img, pix):
    current = start         # Set the current position to the start point
    array = np.array(img)   # Convert the image to a NumPy array for easier manipulation
    path = []               # Initialize a list to store the path taken
    intersects = []         # Initialize a list to store intersecting points
    
    # Continue searching until the current position reaches the end point
    while current != end:
        # Generate possible moves from the current position
        possible = [(current[0]-1, current[1]), (current[0]+1, current[1]),
                    (current[0], current[1]-1), (current[0], current[1]+1)]
        
        # Filter out moves that are walls or have already been visited
        possible = [move for move in possible if pix[move] >= (200, 200, 200) or pix[move] == (0, 9, 254) and pix[move] != (255, 255, 0) and move != start]
        
        # If there are multiple possible moves, add the current position to the list of intersecting points
        if len(possible) >= 2:
            if current not in intersects:
                intersects.append(current)
        
        # If there are no possible moves, backtrack to the last intersection
        if not possible:
            current = intersects.pop()
            path = path[:path.index(current)]
        else:
            # Choose a random move from the list of possible moves
            current = random.choice(possible)
        
        # Add the current position to the path
        path.append(current)
        
        # Mark the current position as visited in the image array
        array[current[1], current[0]] = (255, 255, 0)
    
    # Mark the path in the image array with green pixels
    for p in path:
        array[p[1], p[0]] = (0, 255, 0)
    
    # Convert the modified image array back to an Image object
    img = Image.fromarray(array)
    
    # Save the resulting image
    img.save('image.png')

# Open the maze image
im = Image.open("/Users/FoFa/Downloads/maze_solver/maze-3.png")

# Load pixel data from the image
pix = im.load()

# Find the start and end points in the maze image
start, end = find_ends(im)

# Search for a path from the start to the end point in the maze
search(start, end, im, pix)
