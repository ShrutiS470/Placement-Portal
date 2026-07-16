<template>
  <div class="test">
    <input type="text" placeholder="Enter a message" v-model="this.msg" />
    <button type="button" @click="this.send_post_request">Print</button>
    <h1>Placement Cell:{{ this.msg }}</h1>
    <p>{{ this.res }}</p>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'TestView',
  data(){
    return {
      msg: null,
      res: null,
      token: null,
      role: null
    }
  },
  created(){
      this.token = localStorage.getItem("auth_token")
      this.role = localStorage.getItem("role")
      if (this.token == null) {
        this.$router.push('/login')
      }
      else if(this.role != "student") {
        localStorage.clear()
        this.$router.push('/login')
      }
    },
  methods:{
    print(){
      console.log(this.msg);
      this.msg = null;
    },
    send_post_request(){
        console.log("Sending POST request...");
        axios.post('http://localhost:5000/',{},{
          headers : {
            'Authorization': this.token
        }
        })
        .then(response =>{
            console.log("correct response: ",response)
            this.msg = null
            this.res = response.data.message
        })
        .catch(error =>{
            console.log("error response: ",error)
        })
    }
  }
}
</script>