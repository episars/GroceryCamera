from picamera2 import Picamera2, Preview
import time
from libcamera import Transform
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
still_config = picam2.create_still_configuration(main={"size":(3280,2464)},transform=Transform(hflip=True,vflip=True))
#picam2.configure(camera_config)
#picam2.start_preview(Preview.QTGL)
#picam2.start()
#time.sleep(2)
#picam2.stop()
picam2.configure(still_config)
picam2.start()
image_path = f'/var/www/html/uploads/Groceries.jpg'
picam2.capture_file(image_path)
picam2.stop()
