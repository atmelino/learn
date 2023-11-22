echo git pull

if [ -d "index" ]; then
  cd index
  pwd
  flask run&
  cd ..
fi

if [ -d "data" ]; then
  cd data
  pwd
  flask run -h localhost -p 8989
  cd ..
fi

echo press enter

read input
