<template>
  <div>
    <Row>
        <Col span="12" offset="4">
          <h2 class="h2-title">添加指标</h2>
          <MetricForm
            @submit="handleSubmit"></MetricForm>
        </Col>
    </Row>
  </div>
</template>

<script>
import MetricForm from '@/components/MetricForm.vue'
import {post_metrics} from '@/api/api.js'
export default {
  components: {
    MetricForm
  },
  methods: {
    async handleSubmit(formData) {
      let res = await post_metrics(formData)
      console.log(res)
    }
  }
}
</script>

<style>
.h2-title{
  border-left: 2px solid steelblue;
  padding: 2px 5px;
  display: inline-block;
  margin-bottom: 20px;
}
</style>