// Entry program for the make.fun video-on-X bounty "The agent builds a
// game from one prompt" (Node 22, standard library only).
//
// Its whole job: hand the gate the post's address. It reads POST.json
// from the repository root and writes it, byte for byte, to
// /output/POST.json, where the house reads it. Nothing else is scored:
// the entry is the post itself, and the house reads the post from X.
//
// The POST.json shipped here still holds the placeholder address, so the
// gate refuses it as it stands. Replace it with your post's address
// (https://x.com/<handle>/status/<id>) before you submit.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const source = join(botDir, "POST.json");
const target = join(outDir, "POST.json");

let post: Buffer;
try {
  post = readFileSync(source);
} catch (err) {
  console.error(`cannot read ${source}: ${(err as Error).message}`);
  process.exit(1);
}

try {
  JSON.parse(post.toString("utf8"));
} catch {
  console.error(`${source} is not valid JSON`);
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
writeFileSync(target, post);
