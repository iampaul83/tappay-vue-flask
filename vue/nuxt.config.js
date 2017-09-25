module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'vue',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Nuxt.js project' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ],
    script: [
      { src: 'https://js.tappaysdk.com/tpdirect/v2_2_1' }
    ]
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, ctx) {
      if (ctx.dev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  },
  modules: [
    // Simple usage
  //  '@nuxtjs/proxy',
   
   // With options
   ['@nuxtjs/proxy', { pathRewrite: { '^/api' : '' } }],
  ],
  proxy: {
    // Simple proxy
      '/api': 'http://localhost:5000',
      
      // With options
      // '/api2': { target: 'http://example.com', ws: false }
  }
}
