#!/usr/bin/env python3
"""
Builds /sandsim/index.html into /dist/sandsim.html and updates /dist/index.html.
"""
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "sandsim", "index.html")
DIST_DIR = os.path.join(ROOT, "dist")
DIST_SANDSIM = os.path.join(DIST_DIR, "sandsim.html")

os.makedirs(DIST_DIR, exist_ok=True)
shutil.copy2(SRC, DIST_SANDSIM)
print(f"Built {DIST_SANDSIM} ({os.path.getsize(DIST_SANDSIM):,} bytes)")
