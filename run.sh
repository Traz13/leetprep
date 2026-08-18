#!/usr/bin/env bash
# LeetPrep Local launcher.
set -e
cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
  echo "Setting up (first run only)..."
  python3 -m venv .venv
  ./.venv/bin/pip install -q -r requirements.txt
fi

if ! command -v g++ >/dev/null 2>&1; then
  echo ""
  echo "Note: no C++ compiler ('g++') found on your system."
  echo "The Python track will work fine as-is. To unlock C++:"
  if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "  Run:  xcode-select --install"
  else
    echo "  Run:  sudo apt install build-essential   (or your distro's equivalent)"
  fi
  echo "Then restart this app."
  echo ""
fi

./.venv/bin/python app.py
