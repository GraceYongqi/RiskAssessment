<template>
    <Form :label-width="100">

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
    props: ['risk_indexes'],
    methods: {
        handleSubmit(){
            this.$emit('submit', this.valueArray)
        }
    },
    watch: {
        risk_indexes(){
            this.titleArray = this.risk_indexes
            console.log(this.titleArray, "this.titleArray")
            this.valueArray = [...Array(this.titleArray.length)].map(_=>0);
            this.handleSubmit()
        }
    }
}
</script>