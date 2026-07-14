<template>
    <div class="container mt-5">
    <div class="card shadow p-4 mx-auto" style="max-width: 800px;">     
      <h2 class="text-center text-primary mb-4">
        Application Received
      </h2>
      <div class="card-header bg-primary text-white">
        {{ application.drive.job_title }}
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
</script>