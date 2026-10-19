from picamera2 import Picamera2
from libcamera import Transform
from datetime import datetime
import json
import os
import time

upload_dir = "/var/www/html/uploads"
image_path = os.path.join(upload_dir, "Groceries.jpg")
tmp_image = image_path + ".tmp.jpg"
status_path = os.path.join(upload_dir, "status.json")
tmp_status = status_path + ".tmp"

picam2 = Picamera2()
still_config = picam2.create_still_configuration(
    main={"size": (3280, 2464)},
    transform=Transform(hflip=True, vflip=True),
)
picam2.configure(still_config)
picam2.start()
time.sleep(2)  # let auto-exposure settle

picam2.capture_file(tmp_image)
taken_at = datetime.now().astimezone()  # timezone-aware
picam2.stop()
picam2.close()

# Publish the image, then the timestamp
# Publish the image, then the timestamp
os.chmod(tmp_image, 0o644)
os.replace(tmp_image, image_path)

with open(tmp_status, "w") as f:
    json.dump({"taken_at": taken_at.isoformat()}, f)
os.chmod(tmp_status, 0o644)
os.replace(tmp_status, status_path)
