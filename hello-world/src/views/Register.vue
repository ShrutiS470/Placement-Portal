<template>
  <div class="container mt-5">
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

      <div class="form-check mb-3">
        <input 
          type="checkbox" 
          v-model="isCompany"
          class="form-check-input"
          id="companyCheck"
        />
        <label class="form-check-label" for="companyCheck">
          Register as Company
        </label>
      </div>

      <button 
        type="button"
        class="btn btn-primary w-100 mb-3"
        @click="send_post_request"
      >
        Register
      </button>
      <nav class="d-flex justify-content-between">
        <router-link class="btn btn-outline-secondary btn-sm" to="/login">
          Already have an account? Login
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
      password: "",
      isCompany: false,
      role: ""
    };
  },

  methods: {
    send_post_request() {

      if (this.isCompany) {
        this.role = ["company"];
      } else {
        this.role = ["student"];
      }
      console.log("Sending POST request...");

      axios.post("http://localhost:5000/signup", {
        email: this.email,
        password: this.password,
        role: this.role
      })
      .then(response => {

        console.log("correct response:", response);

        if (response.data.status == "success") {

          this.msg = null;
          this.res = response.data.message;
          localStorage.setItem("user_id", response.data.id);

          if (this.role == "company") {
            this.$router.push('/com_register');
          } 
          else {
            this.$router.push('/stud_register');
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