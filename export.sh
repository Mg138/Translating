#!/usr/bin/sh

python export.py
cd docs
index --modified "Modified" .
touch .nojekyll
cd ..
python md_wrapper.py
./push.sh
read -p "Press enter to continue"
