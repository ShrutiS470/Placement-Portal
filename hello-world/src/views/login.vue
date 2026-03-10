<template>
  <h1>Welcome to Placement Cell</h1>

  <input type="text" placeholder="Email" v-model="email" />
  <input type="password" placeholder="Password" v-model="password" />

  <button type="button" @click="send_post_request">Login</button>

  <nav>
    <router-link to="/com_register">Company Registration</router-link> 
    <router-link to="/stud_register">Student Registration</router-link>
  </nav>
</template>

<script>
import axios from "axios";

export default {
  name: "TestView",

  data() {
    return {
      msg: null,
      res: null,
      email: "",
      password: ""
    };
  },

  methods: {
    send_post_request() {
      console.log("Sending POST request...");

      axios.post("http://localhost:5000/signin", {
        email: this.email,
        password: this.password
      })
      .then(response => {
        console.log("correct response:", response);
        if (response.data.status == "signin successful") {
          localStorage.setItem("auth_token", response.data.auth_token)
          localStorage.setItem("role", response.data.roles)
          this.msg = null
          this.res = response.data.message
          this.$router.push('/test')
        }
      })
      .catch(error => {
        console.log("error response:", error);
      });
    }
  }
};
</script>