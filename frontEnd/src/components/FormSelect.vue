<template>
    <Form :label-width="80">

        <FormItem>
            <Button type="primary" @click="handleSubmit">查询</Button>
        </FormItem>

        <FormItem 
            v-for="(item, index) in titleArray" 
            :key="index" 
            :label="item + index + ' :'">
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
        this.titleArray = [...Array(10)].map(_=>'选项');
        this.valueArray = [...Array(10)].map(_=>0);
        this.handleSubmit()
    }
}
</script>