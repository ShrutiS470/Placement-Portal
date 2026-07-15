<template>
    <div class="card shadow p-4 mx-auto" style="max-width: 400px;">
        <h2 class="text-center text-primary mb-4">{{ drive.job_title }}</h2>
        <p>{{ drive.description }}</p>
        <p><strong>{{ drive.company }}</strong></p>
        <p>Application Deadline: {{ drive.application_deadline }}</p>
        <button v-if="userRole === 'student'" @click="applyNow" class="btn btn-primary btn-sm">
        Apply Now
        </button>
        <button @click="goBack" class="btn btn-outline-secondary btn-sm">
        ← Back
        </button>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: "DriveDetails",
    data() {
        return {
            token: null,
            userRole: null,
            Stu_id: null,
            drive: ""
        };
    },
    created() {
        this.token = localStorage.getItem("auth_token");
        this.userRole = localStorage.getItem("role");
        this.role = localStorage.getItem("role");
        if (this.token == null) {
      this.$router.push("/login");
    } 
    },
    mounted() {
        this.token = localStorage.getItem("auth_token");
        const id = this.$route.params.id;
        axios.get(`http://localhost:5000/drive/${id}`, {
            headers: {
                'Authorization': this.token
            }
        })
        .then(response => {
            console.log("correct response:", response);
            this.drive = response.data;
        })
        .catch(error => {
            console.log("error response:", error);
        });
        
    },
    methods: {
        goBack() {
            this.$router.go(-1);
        },
        applyNow() {
            const stu_id = localStorage.getItem("Student_id");
            const drive_id = this.$route.params.id;
            axios.post('http://localhost:5000/create_application', {
                stu_id: stu_id,
                drive_id: drive_id
            }, {
                headers: {
                    'Authorization': this.token
                }
            })
            .then(response => {
                console.log("Application submitted:", response);
                alert("Application submitted successfully!");
            })
            .catch(error => {
                console.log("Error submitting application:", error);
                alert("Error submitting application. Please try again.");
            });
        }
    },
}
</script>