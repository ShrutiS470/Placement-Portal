<template>
    <div class="card shadow p-4 mx-auto" style="max-width: 400px;">
        <h2 class="text-center text-primary mb-4">{{ drive.job_title }}</h2>
        <p>{{ drive.description }}</p>
        <p><strong>{{ drive.company }}</strong></p>
        <p>Application Deadline: {{ drive.application_deadline }}</p>
        <button v-if="userRole === 'student'" class="btn btn-primary btn-sm">
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
            drive: ""
        };
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
        }
    },
}
</script>