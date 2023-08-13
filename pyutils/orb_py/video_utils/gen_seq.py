import os
import cv2
from tqdm import tqdm

IMG_DIR_NAME = "extracted_images"
TIME_LIST_FILE = "time.txt"

def gen_img_and_timelist(video_path, dump_dir, interval=5):
    if not os.path.exists(video_path):
        raise FileNotFoundError("Video file: {} not found".format(video_path))
    os.makedirs(os.path.join(dump_dir, IMG_DIR_NAME), exist_ok=True)
    videoCapture = cv2.VideoCapture()
    videoCapture.open(video_path)

    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("fps=",fps,"frames=",frames)

    frame_idx = 1
    times = dict()
    for i in tqdm(range(int(frames)), "Extract images from video"):
        ret, frame = videoCapture.read()
        if i % interval == 0:
            cv2.imwrite(
                os.path.join(
                    dump_dir,
                    IMG_DIR_NAME,
                    "{:08d}.png".format(frame_idx)
                ),
                frame
            )
            times[frame_idx] = 1 / fps * frame_idx * interval
            frame_idx += 1
    with open(os.path.join(dump_dir, TIME_LIST_FILE), "w") as time_of:
        for idx in sorted(times.keys()):
            time_of.write("{} {}\n".format(idx, times[idx]))


