#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

def crop():
    # reading image
    image = cv2.imread('equ_imgbb.jpg')

    # converting to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # applying canny edge detection
    edged = cv2.Canny(gray, 10, 250)

    # finding contours
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create a directory to save cropped images
    save_dir = 'cropped/'
    os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist

    # Display the original image with bounding boxes
    cv2.imshow('Bounding Boxes', image)
    cv2.waitKey(0)

    idx = 0
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if w > 50 and h > 50:
            idx += 1
            new_img = image[y:y + h, x:x + w]
            # cropping images
            cv2.imwrite(os.path.join(save_dir, str(idx) + '.png'), new_img)
    print('Objects Cropped Successfully!')
    
    cv2.destroyAllWindows()

# Call the crop function
crop()

