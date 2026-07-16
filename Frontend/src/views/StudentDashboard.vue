<template>
  <div class="container mt-5">
    <div class="card shadow p-4 mx-auto" style="max-width: 800px;">     
      <h2 class="text-center text-primary mb-4">
        Welcome {{ name }}
      </h2>
      <div class="card-header bg-primary text-white">
      Organizations
      <router-link class="btn btn-outline-secondary btn-sm" :to="`/application_history/${user_id}`">
          Application History
        </router-link>
    </div>
      <table class="table table-striped table-hover">
        <tr v-for="com in companies" :key="com.id">
          <td>{{ com.name }}</td>
          <td><router-link class="btn btn-outline-secondary btn-sm" :to="`company_drive/${com.id}`">
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
    name: "StudentView",
    data() {
        return {
            token: null,
            role: null,
            user_id: null,
            student_id: null,
            email: null,
            name: null,
            status: null,
            department: null,
            companies: []
        };
    },
    created() {
        this.token = localStorage.getItem("auth_token");
        this.role = localStorage.getItem("role");
        this.user_id = localStorage.getItem("id");

        if (this.token == null) {
      this.$router.push("/login");
    } else if (this.role != "student") {
      localStorage.clear();
      this.$router.push("/login");
    }
    },
    mounted() {
        const user_id = this.user_id;
        axios.get(`http://localhost:5000/student_dashboard/${user_id}`, {
            headers: {
                'Authorization': this.token
            }
        })
        .then(response => {
            console.log("correct response:", response);
            localStorage.setItem("Student_id", response.data.id);
            this.name = response.data.name;
            this.email = response.data.email;
            this.department = response.data.department;
            this.companies = response.data.companies;
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