<template>
  <div class="container mt-5">
    <div class="card shadow p-4 mx-auto" style="max-width: 400px;">
      
      <h2 class="text-center text-primary mb-4">
        Welcome to Placement Cell
      </h2>

      <input 
        type="text" 
        placeholder="name" 
        v-model="name"
        class="form-control mb-3"
      />

      <input 
        type="text" 
        placeholder="phone" 
        v-model="phone"
        class="form-control mb-3"
      />

      <input 
        type="text" 
        placeholder="degree" 
        v-model="degree"
        class="form-control mb-3"
      />

      <input 
        type="text" 
        placeholder="branch" 
        v-model="branch"
        class="form-control mb-3"
      />

      <input 
        type="text" 
        placeholder="year_of_passing" 
        v-model="year_of_passing"
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

      axios.post("http://localhost:5000/stud_register", {

        user_id: this.user_id,
        name: this.name,
        phone: this.phone,
        degree: this.degree,
        branch: this.branch,
        year_of_passing: this.year_of_passing
      })
      .then(response => {
        console.log("correct response:", response);

        if (response.data.status == "Student registration successful") {
          
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