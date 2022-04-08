chcp 65001
cls
python -m sphinx "./documentation RST/source" "../compiled" -a -E -c "./documentation RST/conf" -T
@ > "../compiled/log.txt"