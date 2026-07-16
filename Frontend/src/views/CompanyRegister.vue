<template>
  <div class="container mt-5">
    <div class="card shadow p-4 mx-auto" style="max-width: 400px;">
      
      <h2 class="text-center text-primary mb-4">
        Welcome to Placement Cell
      </h2>

      <input 
        type="text" 
        placeholder="com_name" 
        v-model="com_name"
        class="form-control mb-3"
      />

      <input 
        type="text" 
        placeholder="website" 
        v-model="website"
        class="form-control mb-3"
      />

      <input 
        type="text" 
        placeholder="industry" 
        v-model="industry"
        class="form-control mb-3"
      />

      <input 
        type="text" 
        placeholder="location" 
        v-model="location"
        class="form-control mb-3"
      />

      <button 
        type="button"
        class="btn btn-primary w-100 mb-3"
        @click="send_post_request"
      >
        Submit
      </button>
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
      user_id:"",
      com_name: "",
      website: "",
      industry: "",
      location: ""
    };
  },
  created() {
    this.user_id = localStorage.getItem("user_id");
  },
  methods: {
    send_post_request() {
      console.log("Sending POST request...");

      axios.post("http://localhost:5000/com_register", {

        user_id: this.user_id,
        com_name: this.com_name,
        website: this.website,
        industry: this.industry,
        location: this.location
      })
      .then(response => {
        console.log("correct response:", response);

        if (response.data.status == "Company registration successful") {
          
          this.msg = null
          this.res = null
          this.$router.push('/login')

          
        }
      })
      .catch(error => {
        console.log("error response:", error);
      });
    }
  }
};
</script>