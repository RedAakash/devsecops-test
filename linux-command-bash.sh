grep '"GET' access.log | awk '{print $1}' | sort | uniq | tee unique_ips.txt | wc -l
