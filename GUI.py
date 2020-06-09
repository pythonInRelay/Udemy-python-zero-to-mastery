#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# name the variables what they are i.e. row, picture, pixel etc. for clarity

for row in picture: # we needed a nested for loop because we're iterating over each item in a matrix
    for pixel in row:   # remember that variable names don't matter, just clarity matters
        if (pixel): # coz truthy we don't need == 1
            print("*", end='') # we're changing default 'new line' to just empty string so it won't print each result on a new line
        else:
            print(" ", end='')
    print('') # final print tells the program after each matrix line THEN print a new line until end