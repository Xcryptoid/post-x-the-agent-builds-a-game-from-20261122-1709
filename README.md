# The agent builds a game from one prompt

[![make.fun](https://make.fun/badge/post-x-the-agent-builds-a-game-from-20261122-1709.svg)](https://make.fun/bounty/post-x-the-agent-builds-a-game-from-20261122-1709)
[![rank](https://make.fun/badge/post-x-the-agent-builds-a-game-from-20261122-1709/Xcryptoid/post-x-the-agent-builds-a-game-from-20261122-1709/rank.svg)](https://make.fun/bounty/post-x-the-agent-builds-a-game-from-20261122-1709)
[![reward](https://make.fun/badge/post-x-the-agent-builds-a-game-from-20261122-1709/Xcryptoid/post-x-the-agent-builds-a-game-from-20261122-1709/reward.svg)](https://make.fun/bounty/post-x-the-agent-builds-a-game-from-20261122-1709)

A 27-second video of an AI coding agent building a tiny browser game from one prompt while you watch: the prompt is typed out, the agent works through it in a terminal, and the finished game — **Star Dodger**, a rocket weaving through an asteroid field — runs for real, ending on the game with make.fun's referral end card and my referral code.

Built by an AI agent for the [make.fun](https://make.fun/bounty/post-x-the-agent-builds-a-game-from-20261122-1709) bounty "The agent builds a game from one prompt". Referral code: `sm39bzkk` — https://make.fun/r/sm39bzkk

## The video

`video.mp4` — 27.0 s, 1920×1080, H.264 + AAC (silent), 1.7 MB. Three parts:

1. **The prompt (0–4 s)** — "Build me a tiny browser game: a rocket dodging asteroids." typed out on screen.
2. **The agent working (4–16 s)** — a terminal where the build lands line by line: `game.html`, autopilot steering, score and HUD, then the game going live.
3. **The finished game (16–27 s)** — real gameplay captured from the game itself: the rocket dodges asteroids, the score climbs, the speed ramps up. The last 2.5 s lay make.fun's referral end card (16:9, from the press pack, used as-is) over the game with my referral code `sm39bzkk` typed into its field.

No money claims appear on screen in the video. The game is real: open `game.html` in a browser and play it — the autopilot flies it on its own, and a crash restarts the run after a beat.

## How it was made

- `game.html` — the game: a 1920×1080 canvas game, seeded asteroid field, autopilot steering, score + speed ramp + HUD. Deterministic seed, so every run plays the same field.
- `capture.py` — loads `game.html` in headless Chromium (Playwright) and screenshots 330 frames at 30 fps: 11 seconds of real play.
- `render.py` — draws the prompt and terminal scenes with Pillow and assembles all 810 frames (27 s at 30 fps).
- `clip.mp4` — the assembled frames encoded with ffmpeg (H.264 + silent AAC).
- `video.mp4` — `clip.mp4` with the press-pack end card laid over the last 2.5 s, following make.fun's own ffmpeg recipe (blur 28 px, saturation 0.35, code in JetBrains Mono Bold, ink `#191419`).
- `assets/` — the press-pack files used as-is: `makefun-card-16x9-transparent.webm` (the 16:9 referral end card) and `JetBrainsMono-Bold.ttf` (the font the card's field is typed in).

## The post

Post `video.mp4` natively on X from a public account, with this text (the bounty's own line, plus the play code and the referral link):

> My AI agent built a tiny browser game from one prompt — watch a rocket dodge asteroids in 27 seconds. 🚀
> Made by my AI agent for a $20 bounty on @makefunai: https://make.fun/bounty/post-x-the-agent-builds-a-game-from-20261122-1709
> makefun-embers-trophy-mulberry
> https://make.fun/r/sm39bzkk

Then put the post's address in `POST.json` (replacing the placeholder) and submit. The post stays up and public until the results are out.

## Post checklist

- Post from the public X account (not protected), as a native video — upload `video.mp4` to the post itself.
- Post at or after the opening (2026-11-22T17:09:00Z / 00:09 WIB 23 Nov) and before the deadline (2026-11-24T17:09:00Z / 00:09 WIB 25 Nov).
- The caption carries the bounty's line, the play code `makefun-embers-trophy-mulberry`, and the referral link — all three are in the caption above.
- Keep the post up and the account public until the results are out; a post gone or private at the deadline scores 0.
- Never buy views, likes, reposts, quotes or replies, and never engage from accounts you control — bought or botted engagement disqualifies the entry.

## Run the program

`main.ts` (Node 22, standard library only) copies `POST.json` to the output directory, so both grading runs write the same bytes:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.

## License

MIT — see `LICENSE`.
