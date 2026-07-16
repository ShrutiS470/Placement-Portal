<template>
    <div class="card shadow p-4 mx-auto" style="max-width: 400px;">
        <h2 class="text-center text-primary mb-4">{{ application.student }}</h2>
        <p>{{ application.department }}</p>
        <p><strong>{{ application.drive }}</strong></p>
        <p> {{ application.company }}</p>
        <div v-if="role === 'company'" class="mb-3">
            <label for="statusDropdown" class="form-label">Status:</label>
            <select id="statusDropdown" v-model="application.status" class="form-select form-select-sm">
                <option value="Applied">Applied</option>
                <option value="Shortlisted">Shortlisted</option>
                <option value="Selected">Selected</option>
                <option value="Rejected">Rejected</option>
            </select>
        </div>
        <p v-else>Status: {{ application.status }}</p>
        <button v-if="role === 'company'" @click="saveStatus" class="btn btn-primary btn-sm">
        Save Status
        </button>
        <button @click="goBack" class="btn btn-outline-secondary btn-sm">
        ← Back
        </button>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: "ApplicationDetails",
    data() {
        return {
            token: null,
            role: null,
            application: ""
        };
    },
    mounted() {
        this.token = localStorage.getItem("auth_token");
        this.role = localStorage.getItem("role");
        const id = this.$route.params.id;
        axios.get(`http://localhost:5000/application/${id}`, {
            headers: {
                'Authorization': this.token
            }
        })
        .then(response => {
            console.log("correct response:", response);
            this.application = response.data;
        })
        .catch(error => {
            console.log("error response:", error);
        });
        
    },
    methods: {
        goBack() {
            this.$router.go(-1);
        },
        saveStatus() {
            const id = this.$route.params.id;
            axios.put(`http://localhost:5000/application/${id}`, {
                status: this.application.status
            }, {
                headers: {
                    'Authorization': this.token
                }
            })
            .then(response => {
                console.log("correct response:", response);
                alert("Status updated successfully!");
            })
            .catch(error => {
                console.log("error response:", error);
                alert("Failed to update status.");
            });
        }
    },
}
</script>