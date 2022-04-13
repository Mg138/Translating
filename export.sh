#!/usr/bin/sh

python export.py
cd docs
index .
touch .nojekyll
cd ..
python md_wrapper.py
./push.sh
read -p "Press enter to continue"
