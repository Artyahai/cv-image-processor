import cv2
from image_finder import find_image_files
from model import BasicImageProcessor


while True:
    
    print('''
          1 - exit,
          2 - grayscale image,
          3 - blur image,
          4 - image rotation
          ''')
    
    num = int(input('Upload photo to this directory and Select tool that you want to use: '))
    
    images = find_image_files()
    images = BasicImageProcessor(images)
    
    if num == 1:
        break 
    
    elif num == 2:
        images.grayscale()
    
    elif num == 3:
        choice = int(input("Which blur do you want? 1 - box blur, 2 - gaussian: "))
        if choice == 1:
        
            coice = False

        elif choice == 2:
        
             choice = True
        second_choice = int(input("Which blur do you want, 1 - weak, 2 - middle, 3 - strong, 4 - strongest: "))

        if second_choice == 1:
        
            second_choice = "weak"

        elif second_choice == 2:
        
            second_choice = "middle"

        elif second_choice == 3:
        
            second_choice = "strong"

        elif second_choice == 4:
        
            second_choice = "strongest"

        else: 
            raise ValueError("please enter only available numbers")
        images.blur(gaussian = choice, blur_level = second_choice)
    
    elif num == 4:
        choice = int(input("Select angle, 1 - 90, 2 - 180: "))
        if choice == 1:
            choice = 90
        
        elif choice == 2:
            choice = 180
        
        second_choice = int(input("select the direction of image rotation (1 - Clockwise, 2 - counterclockwise): "))
        if second_choice == 1:
            second_choice = True

        elif second_choice == 2:
            second_choice = False

        else:
            raise ValueError("please enter only available numbers")
        images.rotate_image(angle=choice, clockwise=second_choice)