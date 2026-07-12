<template>
  <div class="container mt-4">
    <div class="card shadow p-4 mx-auto" style="max-width: 400px;">
      
      <h2 class="text-center text-primary mb-4">
        Welcome to Placement Cell
      </h2>

      <input 
        type="text" 
        placeholder="Email" 
        v-model="email"
        class="form-control mb-3"
      />

      <input 
        type="password" 
        placeholder="Password" 
        v-model="password"
        class="form-control mb-3"
      />

      <button 
        type="button"
        class="btn btn-primary w-100 mb-3"
        @click="send_post_request"
      >
        Login
      </button>

      <nav class="d-flex justify-content-between">
        <router-link class="btn btn-outline-secondary btn-sm" to="/register">
          Don't have an account? Register
        </router-link>
      </nav>

    </div>
  </div>
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
          localStorage.setItem("id", response.data.id)

          this.msg = null
          this.res = response.data.message

          if (response.data.roles.includes("company")) {
            this.$router.push('/com_dashboard');
          } else if (response.data.roles.includes("student")) {
            this.$router.push('/stud_dashboard');
          }else if (response.data.roles.includes("admin")) {
            this.$router.push('/admin_dashboard');
          }
        }
      })
      .catch(error => {
        console.log("error response:", error);
      });
    }
  }
};
</script>