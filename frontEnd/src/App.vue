<template>
  <div id="app">
    <div id="main">
      <router-view/>
    </div>
  </div>
</template>

<style lang="scss">
html,body {
  height: 100%;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  background: #f1f1f1;
}
#main { 
  width: 80%;
  margin: 0 auto;
}

</style>
