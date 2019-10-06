<template>
    <Form :model="formItem" :label-width="80">
        <FormItem label="所属类别">
            <Select v-model="formItem.category">
                <Option 
                    v-for="(lable, index) in enumCategory"
                    :key="index"
                    :value="index + 1">{{lable}}</Option>
            </Select>
        </FormItem>
        <FormItem label="指标名称">
            <Input v-model="formItem.name" placeholder="Enter something..."></Input>
        </FormItem>
        <FormItem label="发生概率">
            <Select v-model="formItem.probability">
                <Option 
                    v-for="(lable, index) in enumLevel"
                    :key="index"
                    :value="lable">{{lable}}</Option>
            </Select>
        </FormItem>
        <FormItem label="影响程度">
            <Select v-model="formItem.impact">
                <Option 
                    v-for="(lable, index) in enumLevel"
                    :key="index"
                    :value="lable">{{lable}}</Option>
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
                enumLevel: Config.enum_level,
                enumCategory: Config.enum_category,
                formItem: {
                    name: 'test',
                    probability: Config.enum_level[1],
                    impact: Config.enum_level[2],
                    category: 2
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
