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
            this.getData(formData)
        },

        getData (formData) {
            let xAxis = ["测试1", "测试2", "测试3", "测试4", "测试5"]
            let yAxis = xAxis.map(v => {
                return parseInt(Math.random()*10) % 8 + 1
            })

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
