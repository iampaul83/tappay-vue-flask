<template>
  <section class="container">
    <div>
      <h1 class="title">TapPay Shop</h1>
      <div class="items">
        <div class="item" v-for="item in items" :key="item.id" @click="$router.push(`/shop/${item.id}`)">
          <div class="name">{{item.name}}</div>
          <div class="amount">NT$ {{item.amount}}</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
export default {
  asyncData ({ params, store }) {
    return axios.get(`http://yujack.com:3000/api/items`)
      .then((res) => {
        const items = Object.keys(res.data).map((key) => {
          const item = res.data[key]
          item.id = key
          return item
        })
        return { items }
      })
  }
}
</script>

<style>
.items {
  margin-top: 30px;
  user-select: none;
  cursor: pointer;
}
.item:hover {
  color: #35495e;
}
.item {
  display: flex;
  padding: 10px;
}
.name {
  flex: 1;
  text-align: right;
}
.amount {
  flex: 1;
  text-align: left;
  margin-left: 10px;
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
</style>
