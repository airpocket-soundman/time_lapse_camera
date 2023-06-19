import os
import cv2

def create_video_from_jpg(folder_path, output_path, fps):
    # フォルダ内のJPGファイルを取得
    file_names = sorted([f for f in os.listdir(folder_path) if f.endswith(".jpg")])
    
    # 1枚目の画像を読み込んで動画の仕様を取得
    first_image_path = os.path.join(folder_path, file_names[0])
    first_image = cv2.imread(first_image_path)
    height, width, channels = first_image.shape
    
    # 動画出力用の設定
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # JPGファイルを読み込んで動画に書き込む
    for file_name in file_names:
        print(file_names,"/",len(file_names))
        file_path = os.path.join(folder_path, file_name)
        image = cv2.imread(file_path)
        video_writer.write(image)
    
    # 動画を保存してリソースを解放
    video_writer.release()

# 入力フォルダのパス
folder_path = "temp"

# 出力動画のパス
output_path = "video.mp4"

# FPS（フレームレート）を指定
fps = 30

# JPGファイルを連結して動画を作成
create_video_from_jpg(folder_path, output_path, fps)
