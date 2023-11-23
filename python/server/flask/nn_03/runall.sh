echo nn


(trap 'kill 0' SIGINT; cd index; pwd; ls; ./run.sh & cd ..; cd data; ./run.sh)

echo press enter

read input
