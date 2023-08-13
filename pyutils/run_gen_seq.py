import argparse

from orb_py.video_utils.gen_seq import gen_img_and_timelist

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=str)
    parser.add_argument("--out_dir", type=str, default="out_seq")
    args = parser.parse_args()
    gen_img_and_timelist(args.video, args.out_dir, 5)

