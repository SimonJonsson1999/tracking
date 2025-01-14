import torch
import cv2
import os

detection_model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

input_video_path = 'football_video.mp4'
output_video_path = 'annotated_football_video.mp4'
output_folder = 'output_frames/'

os.makedirs(output_folder, exist_ok=True)

video = cv2.VideoCapture(input_video_path)
fps = int(video.get(cv2.CAP_PROP_FPS))
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_width, frame_height)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"Processing video with {frame_count} frames at {fps} FPS...")

frame_index = 0

while True:
    ret, frame = video.read()
    if not ret:
        break 

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = detection_model(rgb_frame)

    annotated_frame = results.render()[0] 
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)  

    video_writer.write(annotated_frame)

    output_frame_path = os.path.join(output_folder, f'frame_{frame_index:05d}.jpg')
    cv2.imwrite(output_frame_path, annotated_frame)

    print(f"Processed frame {frame_index + 1}/{frame_count}")
    frame_index += 1

video.release()
video_writer.release()

print(f"Annotated video saved at {output_video_path}")
