rm -r build
rm -r dist

pyinstaller  main.spec --clean
cp ./sgrid.yml ./dist/sgrid.yml

cd dist
tar -zcvf DeepSeekServer.tar.gz ./*
mv ./DeepSeekServer.tar.gz ../
cd ../