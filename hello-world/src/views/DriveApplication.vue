<template>
    <div class="container mt-5">
    <div class="card shadow p-4 mx-auto" style="max-width: 800px;">     
      <h2 class="text-center text-primary mb-4">
        Application Received
      </h2>
      <div class="card-header bg-primary text-white">
        {{ job_title }}
      </div>
      <table class="table table-striped table-hover">
        <tr v-for="app in application":key=app.id>
          <td>{{ app.student }}</td>
          <td><router-link class="btn btn-outline-secondary btn-sm" :to="`/application_details/${app.id}`">
          View Details
        </router-link></td>
        </tr>
      </table>
    </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: "DriveApplicationView",
    data() {
        return {
            token: null,
            role: null,
            id: null,
            job_title: null,
            description: null,
            company: null,
            application_deadline: null,

            status: null,
            application: []
        };
    },
    created() {
        this.token = localStorage.getItem("auth_token");
        this.role = localStorage.getItem("role");
        if (this.token == null) {
      this.$router.push("/login");
    } else if (this.role != "company") {
      localStorage.clear();
      this.$router.push("/login");
    }
    },
    mounted() {
        const id = this.$route.params.id;
        axios.get(`http://localhost:5000/drive_applications/${id}`, {
            headers: {
                'Authorization': this.token
            }
        })
        .then(response => {
            console.log("correct response:", response);
            this.application = response.data.applications;
            this.job_title = response.data.job_title;
            this.description = response.data.job_description;
            this.company = response.data.company;
        })
        .catch(error => {
            console.log("error response:", error);
        });
        
    },
    methods: {
        goBack() {
            this.$router.go(-1);
        }
    },
}
</script>