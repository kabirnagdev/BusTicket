import cv2

valid_tickets = ["T12345|BUS101|2025-09-17"]  
detector = cv2.QRCodeDetector()

# 1. Scan from Image
def scan_from_image(path):
    img = cv2.imread(path)
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        print("Scanned from image:", data)
        if data in valid_tickets:
            print("Ticket Valid")
        else :
            print("Invalid Ticket")
    else:
        print("No QR code found in image")
scan_from_image("bus_ticket.png") 

# 2. Scan from Webcam
cap = cv2.VideoCapture(0)
print("Show QR to camera...")

while True:
    ret, frame = cap.read()
    data, bbox, _ = detector.detectAndDecode(frame)

    if data:
        print("Scanned from webcam:", data)
        if data in valid_tickets:
            print("Ticket Valid")
        else:
            print("Invalid Ticket")
        break

    cv2.imshow("QR Scanner", frame)
    if cv2.waitKey(1) == ord("q"):  # press q to quit
        break

cap.release()
cv2.destroyAllWindows()
