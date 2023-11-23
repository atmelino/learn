echo nn


(trap 'kill 0' SIGINT;  ./run_data.sh & ./run_index.sh)

echo press enter

read input
