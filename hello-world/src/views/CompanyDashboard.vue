<template>
  <div class="container mt-5">
    <div class="card shadow p-4 mx-auto" style="max-width: 800px;">     
      <h2 class="text-center text-primary mb-4">
        Welcome {{ name }}
      </h2>
      <div class="card-header bg-primary text-white">
      Upcoming Drives
      <router-link class="btn btn-outline-secondary btn-sm" :to="`/create_drive`">
          Create New Drive
        </router-link>
    </div>
      <table class="table table-striped table-hover">
        <tr v-for="dr in drives" :key="dr.id">
          <td>{{ dr.job }}</td>
          <td>{{ dr.company }}</td>
          <td><router-link class="btn btn-outline-secondary btn-sm" :to="`/drive_details/${dr.id}`">
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
    name: "CompanyView",
    data() {
        return {
            token: null,
            role: null,
            email: null,
            user_id: null,
            id: null,
            name: null,
            status: null,
            drives: []
        };
    },
    created() {
        this.token = localStorage.getItem("auth_token");
        this.role = localStorage.getItem("role");
        this.user_id = localStorage.getItem("id");

        if (this.token == null) {
      this.$router.push("/login");
    } else if (this.role != "company") {
      localStorage.clear();
      this.$router.push("/login");
    }
    },
    mounted() {
        const user_id = this.user_id;
        axios.get(`http://localhost:5000/company/${user_id}`, {
            headers: {
                'Authorization': this.token
            }
        })
        .then(response => {
            console.log("correct response:", response);
            this.email = response.data.email;
            localStorage.setItem("Com_id", response.data.id);
            this.name = response.data.name;
            this.status = response.data.status;
            this.drives = response.data.drives;
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