<template>
    <Form :model="formItem" :label-width="80">

        <FormItem label="风险等级">
            <Select v-model="formItem.risklevel">
                <Option 
                    v-for="(lable, index) in enumRiskLevel"
                    :key="index"
                    :value="lable">{{lable}}</Option>
            </Select>
        </FormItem>
        <FormItem label="是否发送">
            <Select v-model="formItem.issend">
                <Option 
                    v-for="(lable, index) in enumisSend"
                    :key="index"
                    :value="index">{{lable}}</Option>
            </Select>
        </FormItem>
        <FormItem label="接收方">
            <Select v-model="formItem.receiver">
                <Option 
                    v-for="(lable, index) in enumReceiver"
                    :key="index"
                    :value="index">{{lable}}</Option>
            </Select>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="handleSubmit">提交</Button>
            <Button style="margin-left: 8px">取消</Button>
        </FormItem>
    </Form>
</template>
<script>
    import Config from '@/config/index'
    export default {
        data () {
            return {
                enumRiskLevel: Config.enum_risklevel,
                enumisSend: Config.enum_isSend,
                enumReceiver: Config.enum_receiver,
                formItem: {
                    risklevel: Config.enum_risklevel[0],
                    issend: Config.enum_isSend[0],
                    receiver: Config.enum_receiver[0],
                }
            }
        },
        methods: {
            handleSubmit() {
                this.$emit("submit", this.formItem)
            }
        }
    }
</script>
