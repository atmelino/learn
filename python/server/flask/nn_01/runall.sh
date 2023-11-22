echo nn

# cd index; pwd; ls; ./run.sh & cd ..; cd data; ./run.sh

(trap 'kill 0' SIGINT; cd index; pwd; ls; ./run.sh & cd ..; cd data; ./run.sh)



# if [ -d "index" ]; then
#   cd index
#   pwd
#   flask run&
#   cd ..
# fi

# if [ -d "data" ]; then
#   cd data
#   pwd
#   flask run -h localhost -p 8989
#   cd ..
# fi

echo press enter

read input
