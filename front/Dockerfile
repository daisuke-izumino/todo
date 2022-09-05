FROM node:17.5.0-stretch-slim

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /app

RUN npm install -g npm && \
    npm install -g @vue/cli


# vueアプリが作成されいない状態（初期構築時）は手動で以下のコマンドを実行する
# docker exec -i -t front bash
# vue create .
# yarn add axios vue-axios

# vueサーバーの起動(vueアプリを作成した後、有効化する)。コンテナが起動してから30秒後くらいに起動。
# CMD ["npm", "run", "serve"]