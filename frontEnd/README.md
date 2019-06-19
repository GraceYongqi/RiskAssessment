# riskanalysis 前端运行说明

本目录是风险评估项目的前端目录，结构如下：
```shell

$ tree -L 2
.
|-- README.md
|-- babel.config.js
|-- package-lock.json
|-- package.json             # 前端项目说明文件
|-- postcss.config.js
|-- public
|   |-- favicon.ico
|   |-- index.html
|-- src                      # 前端源代码目录
    |-- App.vue
    |-- api
    |-- assets
    |-- components
    |-- libs
    |-- main.js              # 入口文件
    |-- router.js
    |-- store.js
    `-- views
```


## 操作说明

> 运行本项目前需要安装node环境，[下载地址](http://nodejs.cn/download/)

`npm`为node.js的模块管理工具，类似于centos的yum。为了加快拉取npm包的速度可以使用淘宝镜像。

``` shell
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

### 安装依赖包

```shell
cnpm install # 如没有安装cnpm，则使用npm install
```

### 编译和热重载[开发环境用]

``` shell
npm run serve
```

### 编译和压缩[生产环境用]
```
npm run build
```

### 自定义配置
见 [配置参考](https://cli.vuejs.org/config/).
