from ultralytics import YOLO
from moviepy.editor import VideoFileClip

def resize_video(input_path, output_path, new_width, new_height):
    video = VideoFileClip(input_path)
    resized_video = video.resize((new_width, new_height))
    resized_video.write_videofile(output_path, codec="libx264")


import moviepy.editor as mpe

# Open the video file
video = mpe.VideoFileClip("input_1.avi")

cropped_video = video.crop(x1=420, y1=0, x2=1500, y2=1080)
cropped_video.write_videofile("cropped_video.mp4")
# model = YOLO("runs/detect/train/weights/best.pt")
#resize_video("input_1.avi", "output.mp4", 1, 1080)
model = YOLO("best_from_best.pt")
# model.predict(source="output.mp4", show=True)
model.predict(source= "cropped_video.mp4", show=True,)
# detector = YOLOv8_ObjectDetector(model, conf=0.5, iou=0.45, classes=[39])