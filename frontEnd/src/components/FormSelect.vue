<template>
    <!-- <Form :label-width="100" style="height: 600px; overflow-y: auto;position: relative; padding-top: 60px;">

        <FormItem style="position: absolute; top: 10px; right: 80px;">
            <Button type="primary" @click="handleSubmit">计算风险等级</Button>
        </FormItem>

        <FormItem 
            v-for="(item, index) in titleArray" 
            :key="index" 
            :label="item  + ' :'">
           
            <Select v-model="valueArray[index]">
                <Option 
                    v-for="(lable, index) in enumOccur"
                    :key="index"
                    :value="lable">{{lable}}</Option>
            </Select>
        </FormItem>
    </Form> -->
    <div>
        <Button type="primary" style="position:relative; left: 60px;" @click="handleSubmit">计算风险等级</Button>        
        <Form style="height: 600px; overflow-y: auto;">
            <FormItem 
            v-for="(item, index) in titleArray" 
            :key="index" 
            :label="item  + ' :'">
           
            <Select v-model="valueArray[index]">
                <Option 
                    v-for="(lable, index) in enumOccur"
                    :key="index"
                    :value="lable">{{lable}}</Option>
            </Select>
        </FormItem>
        </Form>
    </div>

</template>
<script>
import Config from '@/config/index'
export default {
    data () {
        return {
            titleArray : [],
            valueArray : [],
            enumOccur:Config.enum_occur,
            formItem: {
                    occur: ''
            }
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
            // this.valueArray = [...Array(this.titleArray.length)].map(_=>0);
            this.valueArray = [...Array(this.titleArray.length)].map(_=>"确定未发生");
            this.handleSubmit()
        }
    }
}
</script>