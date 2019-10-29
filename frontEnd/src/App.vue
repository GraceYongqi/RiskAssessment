<template>
    <div id="app" class="layout page">
        <Layout>
            <Header>
                <Menu mode="horizontal" theme="dark" active-name="1">
                    <div class="layout-logo">审判风险</div>
                    <div class="layout-nav">
                        <MenuItem name="1">
                            <Icon type="ios-navigate"></Icon>
                            <router-link tag="span" :to="{path: '/'}">风险计算</router-link>
                        </MenuItem>
                        <MenuItem name="2">
                            <Icon type="ios-keypad"></Icon>
                            <router-link tag="span" :to="{path: '/MetricManagement'}">指标管理</router-link>
                        </MenuItem>
                        <MenuItem name="3">
                            <Icon type="ios-keypad"></Icon>
                            <router-link tag="span" :to="{path: '/SendManagement'}">推送管理</router-link>
                        </MenuItem>
                    </div>
                </Menu>
            </Header>
            <Layout :style="{padding: '20px 100px'}">
                  <Content :style="{padding: '24px', minHeight: '700px', background: '#fff'}">
                    <router-view/>
                  </Content>
            </Layout>
            <Footer class="layout-footer-center"></Footer>
        </Layout>
    </div>
</div>
</template>
<script>
    export default {
        
    }
</script>
<style scoped>
html,body {
  height: 100%;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#main { 
  width: 100%;
  margin: 0 auto;
}
.page{
  min-height: 100vh;
}
.layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.layout-logo{
    width: 100px;
    border-radius: 3px;
    float: left;
    position: relative;
    line-height: 64px;
    font-size: 24px;
    color: #fff;
}
.layout-nav{
    width: 420px;
    margin: 0 auto;
    margin-right: 20px;
}
.layout-footer-center{
    text-align: center;
}
</style>
