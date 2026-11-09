#!/bin/bash
# Package the build sources into layers-source.zip (no screenshots, videos or backups)
set -e
cd /tmp
OUT=/tmp/w/layers/layers-source.zip; rm -f $OUT
zip -qr $OUT w -x 'w/video/*' 'w/kit/raw/*' 'w/kit/screenshots/*' 'w/review/*' '*/shots/*' '*/__pycache__/*' \
 'w/layers/one/*' 'w/layers/website/*' 'w/layers/layers-source.zip' 'w/*/site/*' 'w/gulf/*/site/*' '*.log' '*.mp4' \
 '*.bak*' '*before*' 'w/*.png' 'w/layers/*.png' 'w/gulf/*/*.png' 'w/*.jpg' 'w/out3.html' 'w/prev*'
zip -q $OUT w/video/*.py
cd /tmp/w && zip -qj $OUT SOURCE.md
ls -la $OUT
