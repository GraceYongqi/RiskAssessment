<template>
    <Form :label-width="80">

        <FormItem>
            <Button type="primary" @click="handleSubmit">计算风险等级</Button>
        </FormItem>

        <FormItem 
            v-for="(item, index) in titleArray" 
            :key="index" 
            :label="item  + ' :'">
            <RadioGroup v-model="valueArray[index]">
                <Radio :label="1">是</Radio>
                <Radio :label="0">否</Radio>
            </RadioGroup>
        </FormItem>

    </Form>
</template>
<script>
export default {
    data () {
        return {
            titleArray : [],
            valueArray : []
        }
    },
    methods: {
        handleSubmit(){
            this.$emit('submit', this.valueArray)
        }
    },
    created () {
        //动态从后端获取指标名称和数量，12不写死
        
        //this.titleArray = [...Array(12)].map(_=>'选项');
        this.titleArray = ['当事人曝光', '媒体报道', '法官自主上报', '社会关注类型', '分案随机', '繁案', '拒绝证据保全', '存在模糊证据', '涉及到赔偿', '被告无法联系', '出现延期审理', '调解失败'];
        this.valueArray = [...Array(12)].map(_=>0);
        this.handleSubmit()
    }
}
</script>