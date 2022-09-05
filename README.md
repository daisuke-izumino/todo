参考資料
https://qiita.com/yota_dev/items/9b4476758341cec2b565


docker起動後

#### frontのコンテナに入る

```
1. sudo docker exec -i -t front bash
```

#### コンテナ内で以下のコマンドを実行axiosなどインストール

```
3. npm install axios && npm install vue-axios
```

#### コンテナ内で移動

```
4. cd todo_app
```

#### コンテナ起動

```
5. npm run serve
```

#### 表示URL

http://localhost





#### docker便利コマンド

コンテナ, image削除コマンド

```
sudo docker rm -f `(sudo docker ps -a)` && sudo docker rmi -f `sudo docker images -a
```
