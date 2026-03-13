<template>
  <div class="container mt-5">
    <div class="card shadow p-4 mx-auto" style="max-width: 800px;">     
      <h2 class="text-center text-primary mb-4">
        Welcome Admin
      </h2>
      <div class="card-header bg-primary text-white">
      Registered Companies
    </div>
      <table class="table table-striped table-hover">
        <tr v-for="comp in company" :key="comp.id">
          <td v-if="comp.status">{{ comp.name }}</td>
        </tr>
      </table>
      <div class="card-header bg-primary text-white">
      Registered Students
    </div>      
      <table class="table table-striped table-hover">
        <tr v-for="stud in student" :key="stud.id">
          <td>{{ stud.name }}</td>
        </tr>
      </table>
      <div class="card-header bg-primary text-white">
      Company Applications
    </div>
      <table class="table table-striped table-hover">
        <tr v-for="comp in company" :key="comp.id">
          <td v-if="comp.status !== true">{{ comp.name }}</td>
        </tr>
      </table>
      <div class="card-header bg-primary text-white">
      Ongoing Drives
    </div>
      <table class="table table-striped table-hover">
        <tr v-for="dr in drive" :key="dr.id">
          <td>{{ dr.job }}</td>
          <td>{{ dr.company }}</td>
          <td><router-link class="btn btn-outline-secondary btn-sm" :to="`/drive_details/${dr.id}`">
          View Details
        </router-link></td>
        </tr>
      </table>
      <div class="card-header bg-primary text-white">
      Student Applications
    </div>
      <table class="table table-striped table-hover">
        <tr v-for="app in application":key=app.id>
          <td>{{ app.student }}</td>
          <td>{{ app.drive }}</td>
          <td>{{ app.company }}</td>
          <td><router-link class="btn btn-outline-secondary btn-sm" :to="`/application_details/${app.id}`">
          View Details
        </router-link></td>
        </tr>
      </table>
      </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
  name: "TestView",
  data() {
    return {
      token: null,
      role: null,
      company: [],
      student: [],
      drive: [],
      application: []
    };
  },
  created(){
    this.token = localStorage.getItem("auth_token");
    this.role = localStorage.getItem("role");

    if (this.token == null) {
      this.$router.push("/login");
    } else if (this.role != "admin") {
      localStorage.clear();
      this.$router.push("/login");
    }
  },
  mounted() {
    console.log("Sending GET request...")
    axios.get("http://localhost:5000/admin", {
      headers: { 'Authorization': this.token }
        })
      .then(response => {

        console.log("correct response:", response)
        this.company = response.data.companies;
        this.drive = response.data.drives;
        this.student = response.data.students;
        this.application = response.data.applications;
          })
      .catch(error => {
        console.log("error response:", error);
      });

    }
  }
</script>