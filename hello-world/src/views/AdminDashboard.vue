<template>
  <div class="container mt-5">      
      <h2 class="text-center text-primary mb-4">
        Welcome Admin
      </h2>
      <table>
        <thead>Registered Company</thead>
        <tr v-for="comp in company" :key="comp.id">
          <td v-if="company.status">{{ company.name }}</td>
        </tr>
      </table>
      
      <table>
        <thead>Registered Students</thead>
        <tr v-for="stud in student" :key="stud.id">
          <td>{{ stud.name }}</td>
        </tr>
      </table>

      <table>
        <thead>Company Application</thead>
        <tr v-for="comp in company" :key="comp.id">
          <td v-if="comp.status !== true">{{ comp.name }}</td>
        </tr>
      </table>

      <table>
        <thead>Ongoing Drive</thead>
        <tr v-for="dr in drive" :key="dr.id">
          <td>{{ dr.job }}</td>
          <td>{{ dr.company }}</td>
        </tr>
      </table>
      
      <table>
        <thead>Student Application</thead>
        <tr v-for="app in application":key=stu.id>
          <td>{{ app.student }}</td>
          <td>{{ app.drive }}</td>
          <td>{{ company }}</td>
        </tr>
      </table>
      
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
    axios.get("http://localhost:5000/admin",{
        headers : {
          'Authentication-Token': this.token
        }
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