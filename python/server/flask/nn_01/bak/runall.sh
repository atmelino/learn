echo git pull

function process_index() {
  cd index
  pwd
  flask run
  cd ..
}

function process_data() {
  cd data
  pwd
  flask run
  cd ..
}

#(trap 'kill 0' SIGINT; process_index()& process_data())
(trap 'kill 0' SIGINT; cd index;pwd;flask run& cd ..   cd data;pwd;flask run;cd ..)


echo press enter

read input
