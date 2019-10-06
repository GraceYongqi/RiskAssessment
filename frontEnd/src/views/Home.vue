<template>
    <Row class="main-box" :gutter="16">
        <Col :span="6">
            <Card dis-hover>
                <p slot="title">
                    <Icon type="ios-american-football-outline" />
                    风险指标
                </p>
                <form-select :risk_indexes="risk_indexes" @submit="handleFormSelect"></form-select>
            </Card>
        </Col>

        <Col :span="18">
            <Card dis-hover >
                <chart :value="value"></chart>
            </Card>
        </Col>
    </Row>
</template>
<script>
import Chart  from '../components/Chart'
import FormSelect from '../components/FormSelect'
import {compute_level_risk, get_metrics} from '../api/api.js'

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
            value : {},
            risk_indexes: []
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
            let xAxis = ["舆情风险", "质量风险", "效率风险", "廉政风险"]
            let yAxis = res.data.map(v => rish_map[v]) || [1,2,3,4]

            this.updateFigure({xAxis, yAxis})
        },

        updateFigure (data = {}) {
            this.value = data
        },

        async getMetrics() {
            let res = await get_metrics()
            console.log(typeof res.risk_indexes, res)
            this.$set(this, 'risk_indexes', res.risk_indexes)
        }
    },
    async created() {
        compute_level_risk()
        await this.getMetrics()
    },
}
</script>
<style lang="scss">
    .main-box{height: 100%; align-items:stretch;}
</style>
