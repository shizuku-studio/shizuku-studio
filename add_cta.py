from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import os

INPUT  = r"D:\Claude-MyProject\shizuku-studio\hero-video.mp4"
OUTPUT = r"D:\Claude-MyProject\shizuku-studio\x-post-video.mp4"
FONT   = r"C:\Windows\Fonts\BIZ-UDGothicR.ttc"

video = VideoFileClip(INPUT)
W, H = video.size  # 1080x1920
dur = video.duration  # 15s

gold  = "#C8A84B"
white = "#FFFFFF"

def txt(text, size, color, y_pos, t0, t1):
    clip = TextClip(
        text=text,
        font=FONT,
        font_size=size,
        color=color,
        stroke_color="black",
        stroke_width=3,
    )
    cx = (W - clip.w) // 2
    return clip.with_position((cx, y_pos)).with_start(t0).with_end(t1)

layers = [
    video,
    txt("しずく AI Studio",                    52, gold,  80,      0, dur),
    txt("AIで変わりたいあなたへ",              62, white, H - 310, 0,   8),
    txt("素顔を守りながら  AIで美しく",         56, white, H - 360, 8,  dur),
    txt("LINE公式へ「応募(おうぼ)」と送るだけ", 52, gold,  H - 160, 12, dur),
]

final = CompositeVideoClip(layers)
final.write_videofile(
    OUTPUT,
    codec="libx264",
    audio_codec="aac",
    fps=video.fps,
)
print("完了:", OUTPUT)
