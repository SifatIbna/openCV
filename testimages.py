import cv2

img = cv2.imread('test images/batman.jpg')

while True:
    cv2.imshow('Batman',img)
    
    # If we've waited at least 1ms AND we've pressed the ESC key
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()