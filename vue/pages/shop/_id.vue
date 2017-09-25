<template>
  <section class="container">
    <div>
      <h1 class="title">{{item.name}}</h1>
      <h2 class="subtitle">NT$ {{item.amount}}</h2>
      <div id="cardview-container">
        <div id="card"></div>
        <button @click="pay">Pay</button>
      </div>
      <div id="pay-result" v-if="payResult">{{payResult}}</div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      payResult: undefined
    }
  },
  asyncData ({ params }) {
    return axios.get(`http://yujack.com:3000/api/items/${params.id}`)
      .then((res) => {
        return { item: res.data }
      })
  },
  mounted () {
    TPDirect.setupSDK(10985, 'app_x43v5VnvPVyaQ42KVZpRUTtiUlwVL3IkDYTcbAQ17qwuZAkwjQZfsu515glx', 'sandbox')
    TPDirect.card.setup('#card')
  },
  methods: {
    pay () {
      TPDirect.card.getPrime((result) => {
        if (result.status !== 0) {
          console.error('getPrime 錯誤')
          return
        }
        const prime = result.card.prime
        console.log('getPrime 成功: ' + prime)
        console.log(this.$route.params)
        axios.post(`http://yujack.com:3000/api/pay/${this.$route.params.id}`, { prime })
          .then((res) => {
            console.log(res.data)
            this.payResult = res.data
          })
      })
    }
  }
}
</script>

<style>
#pay-result {
  max-width: 330px;
  margin: 0 auto;
  margin-top: 30px;
}
#cardview-container {
  max-width: 330px;
  margin: 0 auto;
}
#card {
  padding: 5px 10px;
  border: 1px solid rgba(82, 100, 136, .5);
  margin-bottom: 10px;
}
#cardview-container > button {
  width: 100%;
  border: none;
  padding: 10px;
  border-radius: 5px;
  font-size: 15px;
  background-color: rgba(82, 100, 136, .2);
}
.container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; /* 1 */
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}
.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}
</style>
