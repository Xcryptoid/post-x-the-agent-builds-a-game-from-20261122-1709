"""Render the video's text scenes and assemble the full frame sequence.

- Frames 0-119 (4 s): the prompt, typed out character by character.
- Frames 120-479 (12 s): the agent working — terminal lines appear one by one.
- Frames 480-809 (11 s): real gameplay frames captured by capture.py.
All frames are 1920x1080 PNGs in frames/final/, 30 fps, 810 frames = 27 s.
"""
import os
import shutil

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FINAL = os.path.join(HERE, "frames", "final")
GAMEPLAY = os.path.join(HERE, "frames", "gameplay")
os.makedirs(FINAL, exist_ok=True)

W, H = 1920, 1080
BG = (5, 7, 15)
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


# ---------------------------------------------------------------- prompt scene
PROMPT_LINES = ["Build me a tiny browser game:", "a rocket dodging asteroids."]
PROMPT_TEXT = "\n".join(PROMPT_LINES)


def prompt_frame(step):
    """step 0..29: typing progress; 30 = done + bottom line."""
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    f_label = font(MONO, 36)
    f_big = font(MONO_BOLD, 64)
    f_small = font(MONO, 36)
    d.text((200, 90), "ONE PROMPT", fill=(107, 114, 128), font=f_label)
    total = sum(len(l) for l in PROMPT_LINES)
    shown = total if step >= 29 else min(total, int(total * step / 30) + 1)
    y = 420
    remaining = shown
    cursor = None
    for li, line in enumerate(PROMPT_LINES):
        take = min(len(line), remaining)
        color = (232, 236, 244) if li == 0 else (56, 189, 248)
        d.text((200, y), line[:take], fill=color, font=f_big)
        if take < len(line):
            w = d.textlength(line[:take], font=f_big)
            cursor = (200 + w, y)
            break
        remaining -= take
        y += 110
    else:
        cursor = (200 + d.textlength(PROMPT_LINES[-1], font=f_big), 420 + 110)
    if cursor and step % 2 == 0:
        d.rectangle([cursor[0] + 8, cursor[1] + 8, cursor[0] + 40, cursor[1] + 72],
                    fill=(74, 222, 128))
    if step >= 29:
        d.text((200, 700), "my AI agent is building it — watch",
               fill=(156, 163, 175), font=f_small)
    return img


# -------------------------------------------------------------- terminal scene
TERM_LINES = [
    ("$ ", "agent ← one prompt: build a tiny browser game", "cmd"),
    ("✓ ", "game.html — canvas 1920×1080, rocket + asteroids", "ok"),
    ("✓ ", "autopilot steering, seeded asteroid field", "ok"),
    ("✓ ", "score, speed ramp, HUD", "ok"),
    ("✓ ", "220 stars, parallax drift", "ok"),
    ("$ ", "node: running it — watch it fly", "cmd"),
    ("▶ ", "STAR DODGER is live", "go"),
    ("▶ ", "your turn: come build on make.fun", "go"),
]
TERM_COLORS = {"cmd": (74, 222, 128), "ok": (74, 222, 128), "go": (251, 191, 36)}


def terminal_frame(step):
    """step 0..11: one line appears per 1.5 s (45 frames each)."""
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # Window.
    d.rounded_rectangle([140, 120, 1780, 960], radius=24,
                        fill=(13, 17, 23), outline=(31, 41, 55), width=2)
    d.ellipse([180, 158, 204, 182], fill=(255, 95, 86))
    d.ellipse([216, 158, 240, 182], fill=(255, 189, 46))
    d.ellipse([252, 158, 276, 182], fill=(39, 201, 63))
    d.text((300, 152), "agent — star-dodger", fill=(156, 163, 175),
           font=font(MONO, 32))
    f = font(MONO, 38)
    f_bold = font(MONO_BOLD, 38)
    y = 230
    visible = min(len(TERM_LINES), step // 45 + 1) if step < 360 else len(TERM_LINES)
    for i in range(visible):
        mark, text, kind = TERM_LINES[i]
        d.text((200, y), mark, fill=TERM_COLORS[kind], font=f_bold)
        w = d.textlength(mark, font=f_bold)
        d.text((200 + w, y), text, fill=(229, 231, 235), font=f)
        y += 76
    if step % 2 == 0:
        d.rectangle([200, y + 8, 228, y + 44], fill=(74, 222, 128))
    return img


def main():
    n = 0
    # Prompt: 4 s, 30 typing steps, 4 frames each.
    for step in range(30):
        img = prompt_frame(step)
        for _ in range(4):
            img.save(os.path.join(FINAL, "%04d.png" % n))
            n += 1
    # Terminal: 12 s, 8 lines x 45 frames.
    for step in range(8):
        img = terminal_frame(step * 45)
        for _ in range(45):
            img.save(os.path.join(FINAL, "%04d.png" % n))
            n += 1
    # Gameplay: 330 captured frames.
    for i in range(330):
        src = os.path.join(GAMEPLAY, "%04d.png" % i)
        shutil.copy(src, os.path.join(FINAL, "%04d.png" % n))
        n += 1
    print("assembled %d frames (%.1f s at 30 fps)" % (n, n / 30))


if __name__ == "__main__":
    main()
