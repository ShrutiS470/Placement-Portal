<template>
  <div class="container mt-5">
    <div class="card shadow p-4 mx-auto" style="max-width: 400px;">
      
      <h2 class="text-center text-primary mb-4">
        Create New Drive
      </h2>

      <input 
        type="text" 
        placeholder="Job Title" 
        v-model="job_title"
        class="form-control mb-3"
      />

      <input 
        type="text" 
        placeholder="Job Description" 
        v-model="job_description"
        class="form-control mb-3"
      />

      <input 
        type="text" 
        placeholder="Eligibility Criteria" 
        v-model="eligibility_criteria"
        class="form-control mb-3"
      />

      <input 
        type="text" 
        placeholder="application Deadline (YYYY-MM-DD)" 
        v-model="application_deadline"
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
  name: "CreateDriveView",

  data() {
    return {
      msg: null,
      res: null,
      token: null,
      com_id:"",
      job_title: "",
      job_description: "",
      eligibility_criteria: "",
      application_deadline: ""
    };
  },
  created() {
    this.token = localStorage.getItem("auth_token");
    this.com_id = localStorage.getItem("Com_id");

    console.log("Token:", this.token);
    console.log("Company ID:", this.com_id);
  },
  methods: {
    send_post_request() {
      console.log("Sending POST request...");
      axios.post("http://localhost:5000/create_drive", {
        com_id: this.com_id,
        job_title: this.job_title,
        job_description: this.job_description,
        eligibility_criteria: this.eligibility_criteria,
        application_deadline: this.application_deadline
      }, {
        headers: {
          'Authorization': this.token
        }
      })
      .then(response => {
        console.log("correct response:", response);

        if (response.data.message == 'Drive created successfully') {
          
          this.msg = null
          this.res = null
          this.$router.push('/com_dashboard')

          
        }
      })
      .catch(error => {
        console.log("error response:", error);
      });
    }
  }
};
</script>