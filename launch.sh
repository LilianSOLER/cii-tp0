rm data/*
./trace2.py -o data/cos.ps -X 10 -n $1 "cos(x)"
gs data/cos.ps