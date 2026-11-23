"""Capture real gameplay frames of Star Dodger for the video.

Loads game.html in headless Chromium, lets the autopilot fly for a beat,
then screenshots 30 fps for 11 seconds (330 frames, 1920x1080 PNG).
(Screenshots, not video recording: the recorder came back black here.)
"""
import os
import time

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FRAMES = os.path.join(HERE, "frames", "gameplay")
os.makedirs(FRAMES, exist_ok=True)

FPS = 30
SECONDS = 11
N = FPS * SECONDS

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto("file://" + os.path.join(HERE, "game.html"))
    page.wait_for_timeout(1500)  # let the field fill and the ship settle
    start = time.time()
    for i in range(N):
        page.screenshot(path=os.path.join(FRAMES, "%04d.png" % i))
        # Pace to ~30 fps; screenshot itself takes ~40-80 ms.
        target = start + (i + 1) / FPS
        sleep = target - time.time()
        if sleep > 0:
            time.sleep(sleep)
    print("captured %d frames in %.1fs" % (N, time.time() - start))
    browser.close()
