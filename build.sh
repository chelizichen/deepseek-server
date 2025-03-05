rm -r build
rm -r dist

pyinstaller  main.spec --clean
cp ./sgrid.yml ./dist/sgrid.yml

cd ./dist
tar -zcvf DeepSeekBackServer.tar.gz ./*
mv ./DeepSeekBackServer.tar.gz ../
cd ../