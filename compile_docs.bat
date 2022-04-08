chcp 65001
cls
python -m sphinx "./documentation RST/source" "../compiled" -a -E -c "./documentation RST/source" -T
@ > "../compiled/log.txt"