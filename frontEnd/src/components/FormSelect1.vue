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
                <Radio :label="确定发生">是</Radio>
                <Radio :label="确定未发生">否</Radio>
            </RadioGroup>
            <!-- <Select v-model="valueArray[index]">
                <Option 
                    v-for="(lable, index) in occurs"
                    :key="index"
                    :value="lable">{{lable}}</Option>
            </Select> -->
        </FormItem>

    </Form>
</template>
<script>
import Config from '@/config/index'
export default {
    data () {
        return {
            occurs: Config.enum_occur,
            titleArray : [],
            // valueArray : []
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
            this.valueArray = [...Array(this.titleArray.length)].map(_=>"确定未发生");
            this.handleSubmit()
        }
    }
}
</script>