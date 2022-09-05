こちらを参照
https://qiita.com/yota_dev/items/9b4476758341cec2b565


DB構成

vue URL

http://localhost/80

docker起動後

frontのコンテナに入る
```
1. sudo docker exec -i -t front bash
```

コンテナ内で以下のコマンドを実行
```
3. npm install axios && npm install vue-axios
```

コンテナ内で移動
```
4. cd todo_app
```

コンテナ起動
```
5. npm run serve
```

dockerお掃除 
```
sudo docker rm -f `(sudo docker ps -a)` && sudo docker rmi -f `sudo docker images -a
```# TODO
