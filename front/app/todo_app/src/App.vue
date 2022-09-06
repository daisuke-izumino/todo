<template>
  <div id="app">
    <h1>Todoリスト</h1>
    <p>タイトル</p>
    <input v-model="title" /><br />
    <p>内容</p>
    <textarea v-model="text"></textarea><br />
    <button @click="addTodo()">追加</button>
    <p>{{ task_id }}</p>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>タイトル</th>
          <th>内容</th>
          <th>削除</th>
        </tr>
      </thead>
      <tr v-for="(todo, index) in info" :key="index">
        <td>{{ todo.task_id }}</td>
        <td>{{ todo.title }}</td>
        <td>{{ todo.text }}</td>
        <td><button @click="deleteTodo(index)">削除</button></td>
      </tr>
    </table>
  </div>
</template>

<script>
import { axios } from "../plugins/axios";

export default {
  data() {
    return {
      msg: "はじめまして",
      info: null,
      task_id: "",
      title: "",
      text: "",
    };
  },
  mounted() {
    this.get_hoge().then((response) => {
      this.info = "";
      this.info = response.data;
    });
  },
  methods: {
    get_hoge() {
      return axios.get("task");
    },
    post_hoge() {
      return axios.post("task", {
        title: this.title,
        text: this.text,
      });
    },
    addTodo: function () {
      if (this.title == "" || this.text == "") {
        window.alert("必要項目の確認");
      } else {
        this.post_hoge().then((response) => {
          this.info.push(response.data);
        });
        (this.title = ""), (this.text = "");
      }
    },
    deleteTodo: function (index) {
      if (window.confirm("本当に削除しますか")) {
        return axios.post("task/delete", {
          task_id: this.info.splice(index, 1)[0].task_id,
        });
      }
    },
  },
};
</script>

<style>
#app ul {
  list-style: none;
}

#app input,
textarea {
  font-size: 1em;
  padding: 15px 5px 10px;
  font-family: "Source Sans Pro", arial, sans-serif;
  border: 1px solid #cecece;
  background: #8f8d8d;
  color: #fafafa;
  box-sizing: border-box;
  width: 30%;
  max-width: 600px;
}
</style>
