<template>
    <Row class="main-box" :gutter="16">
        <Col :span="6">
            <Card>
                <p slot="title">
                    <Icon type="ios-american-football-outline" />
                    选择区
                </p>
                <form-select @submit="handleFormSelect"></form-select>
            </Card>
        </Col>

        <Col :span="18">
            <Card>
                <chart :value="value"></chart>
            </Card>
        </Col>
    </Row>
</template>
<script>
import Chart  from '../components/Chart'
import FormSelect from '../components/FormSelect'
import {compute_level_risk} from '../api/api.js'

let rish_map = {
    'absolutely low'  :   1,
    'very low'        :   2,
    'low'             :   3,
    'fairly low'      :   4,
    'medium'          :   5,
    'fairly high'     :   6,
    'high'            :   7,
    'very high'       :   8,
    'absolutely high' :   9
}

export default {
    components: {
        Chart,
        FormSelect
    },
    data () {
        return {
            value : {}
        }
    },
    methods: {
        handleFormSelect (formData) {
            console.log("筛选")
            this.getData(formData)
        },

        async getData (formData) {
            console.log(formData)
            let res = await compute_level_risk(formData)
            let xAxis = ["测试1", "测试2", "测试3", "测试4"]
            let yAxis = res.data.map(v => rish_map[v]) || [1,2,3,4]

            this.updateFigure({xAxis, yAxis})
        },

        updateFigure (data = {}) {
            this.value = data
        }
    },
    created() {
        compute_level_risk()
    },
}
</script>
<style lang="scss">
    .main-box{height: 100%; align-items:stretch;}
</style>
