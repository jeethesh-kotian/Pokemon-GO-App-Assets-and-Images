# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("Pokemon Models (PNG Format)")):
        renamedFilename = filename[0:3] + ".png"
        src = os.path.join('Pokemon Models (PNG Format)', filename )
        dst = os.path.join('PokemonModelsRenamed', renamedFilename )
        print(src + " to " + dst)
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 