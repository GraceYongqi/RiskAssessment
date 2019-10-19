<template>
  <div>
    <Row>
        <Col span="12" offset="4">
          <h2 class="h2-title">修改推送方式</h2>
          <MethodForm
            @submit="handleSubmit"></MethodForm>
        </Col>
    </Row>
  </div>
</template>

<script>
import MethodForm from '@/components/MethodForm.vue'
import {post_method} from '@/api/api.js'
export default {
  components: {
    MethodForm
  },
  methods: {
    async handleSubmit(formData) {
      let res = await post_method(formData)
      console.log(res)
      alert("修改成功！")
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