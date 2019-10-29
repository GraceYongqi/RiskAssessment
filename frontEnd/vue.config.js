module.exports = {
    // 修改的配置
    // 将baseUrl: '/api',改为baseUrl: '/',
    baseUrl: '/static',
    devServer: {
        proxy: {
            '/': {
                target: 'http://localhost:8888',
                changeOrigin: true,
                ws: true,
                // pathRewrite: {
                //   '^/api': ''
                // }
            }
        }
    }
}




