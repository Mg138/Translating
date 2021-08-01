python export.py
cd docs
index --title "檢索中: #DIR" --parent_dir "往上一層" --filename "檔案名稱" --size "大小" --modified "最後修改日期" .
touch .nojekyll
cd ..
python md_wrapper.py
./push.sh
read -p "Press enter to continue"
