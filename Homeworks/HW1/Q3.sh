cat < filename | tr " " "\n" | sort | uniq | wc -w