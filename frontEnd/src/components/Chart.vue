<template>
    <div>
        <div ref='echartDom' style="width: 100%; min-height:600px;"></div>
    </div>
</template>

<script>
let levelMap = ['', 'absolutely low', 'very low', 'low', 'fairly low', 'medium', 'fairly high', 'high', 'very high', 'absolutely high']

export default {   
    data () {
        return {
            myChart: {},
            options: {
                legend: {
                    
                },
                tooltip: {
                    formatter: function (obj) {
                        return '<div style="font-size: 14px;padding-bottom: 7px;margin-bottom: 7px">'
                            + `${obj.name} : level${obj.value}(${levelMap[obj.value]})</div>`;
                    }
                },
                title: {
                    text: '风险预警等级',
                },
                visualMap: {
                    top: 0,
                    right: 0,
                    show: false,
                    categories: ['absolutely low', 'very low', 'low', 'fairly low', 'medium', 
                        'fairly high', 'high', 'very high', 'absolutely high'],
                    pieces: [
                        {gte: 8, lte: 9, color: 'red'},
                        {gte: 6, lte: 7, color: 'orange'},
                        {gte: 3, lte: 5, color: 'yellow'}
                    ],
                    inRange: {
                        color: '#f00'
                    },
                    backgroundColor : '#f1f1f1'
                },
                xAxis : {
                    type : 'category',
                    name : '风险类别',
                    data : [],
                },
                yAxis: {min: 0, max: 9, name: '风险等级'},
                series : [
                    {
                        type:'bar',
                        data:[]
                    }
                ],
                animationDuration: 2000
            }
        }
    },
    methods: {
        updateOptions(xAxis=[], yAxis=[]){
            let options = {
                xAxis: {
                    data: xAxis
                },
                series: [{
                    // 根据名字对应到相应的系列
                    name: '风险等级',
                    data: yAxis
                }]
            }
            this.myChart.setOption(options)
        }
    },
    props: {
        value: Object
    },
    watch: {
        value: {
            handler: function (val, oldVal) { 
                console.log("value 变了")
                this.updateOptions(val.xAxis, val.yAxis)
            },
            deep: true
        }
    },
    mounted() {
        this.myChart = this.$echarts.init(this.$refs.echartDom)
        this.myChart.setOption(this.options)
    }
}
</script>