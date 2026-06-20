from PIL import Image,UnidentifiedImageError
import numpy as np
import tqdm,sys

file = input("Enter image filename: ")

def output(z):
    out = z.astype(np.uint8)
    img = Image.fromarray(out)
    img.save("output.png")
    print("Your image with filters applied is saved successfully.")

print("=======================================\n|         IMAGE FILTER STUDIO         |\n=======================================")

while True:
    try:
        image = Image.open(file)
    except FileNotFoundError:
        print("Image not found.")
        sys.exit()
    except UnidentifiedImageError:
        print("Invalid image file.")
        sys.exit()
    iarray = np.array(image) 
    arr = iarray.astype(np.float32)
    
    print(f" 📁 Loaded Image :- {file} \n 📏 Resolution :- {image.size} \n 🎨 Channels :- {image.mode}")
    print("--------------------------------------- ")
    print("Available Filters\n")
    print("Press 1: Brightness")
    print("Press 2: Contrast")
    print("Press 3: Grayscale")
    print("Press 4: Crop")
    print("Press 5: Remove Red Channel")
    print("Press 6: Remove Green Channel")
    print("Press 7: Remove Blue Channel")
    print("Press 8: Blur")
    while True:
        try:
            check = int(input("Please enter a choice :- "))
            if check in [1,2,3,4,5,6,7,8]:
                break
            else:
                print("Please give a valid response.")
        except:
            print("Please enter a vaild response.")
    if(check==1):
        x = int(input("By how much do you want to increase the brightness of image(Give an integer):- "))
        bri = arr + x
        result = np.clip(bri, 0, 255)   
        output(result)
        
    elif(check==2):
        while True:
            x = float(input("Contrast factor (>0): "))
            if x > 0:
                break
            print("Please enter a value greater than 0.")
        contrast = 128 + (arr - 128) * x
        result = np.clip(contrast, 0, 255)
        output(result)
        
    elif(check==3):
        result = np.round(arr @ [0.299, 0.587, 0.114])
        output(result)
        break
        
    elif(check==4):
        width=int(input("The width of cropped image (in pixels):- "))
        height = int(input("The height of cropped image (in pixels):-"))
        if width > image.size[0] or height > image.size[1]:
            print("Crop size exceeds image dimensions.")
            continue
        widt1 = int(round((image.size[0]/2)-(width/2)))
        widt2 = int(round((image.size[0]/2)+(width/2)+1))
        heigh1 = int(round((image.size[1]/2)-(height/2)))
        heigh2 = int(round((image.size[1]/2)+(height/2)+1))
        result = arr[heigh1:heigh2,widt1:widt2]
        output(result)
        
    elif(check==5):
        result = np.round(arr * [0,1,1])
        output(result)
        
    elif(check==6):
        result = np.round(arr *[1,0,1])
        output(result) 
        
    elif(check==7):
        result = np.round(arr * [1,1,0])
        output(result)
        
    elif(check==8):
        blur = arr.copy()

        h, w, c = arr.shape

        for i in tqdm.tqdm(range(1, h-1)):
            for j in range(1, w-1):
                area = arr[i-1:i+2, j-1:j+2]
                blur[i, j] = np.mean(area, axis=(0,1))

        blur = np.clip(blur, 0, 255)
        output(blur)

    while True:        
        print("Press 1 : Add filters")
        print("Press 2 : Save and EXIT")

        try:
            you = int(input("Your response :-"))
        except:
            print("Please enter a valid response.")
            continue
        if(you==2):
            print("Thanks for using.")
            sys.exit()
        elif(you==1):
            file = "output.png"
            break
        else:
            print("Please Enter a valid response.")    