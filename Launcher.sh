cat ./server.conf > ./exec.tmp
cat $1 >> ./exec.tmp
./exec.tmp
