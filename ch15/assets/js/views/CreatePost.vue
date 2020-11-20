<template>
  <div class="container app__container">
    <form class="post-form">
      <!-- 编剧帖子标题，绑定到 form.title -->
      <div class="form-group">
        <input
          type="text"
          placeholder="标题"
          class="post-title"
          v-model="form.title"
        />
      </div>
      <!-- 选择帖子话题, 绑定到 form.topic_name -->
      <div class="form-group post-topic">
        <select v-model="form.topic_name"
          ><option v-for="topic in topics">{{ topic.name }}</option></select
        >
      </div>
      <!-- 编辑帖子内容, 绑定到 form.content -->
      <div class="form-group">
        <textarea
          rows="25"
          placeholder="想说些什么..."
          v-model="form.content"
          v-if="!isPreview"
        ></textarea>
       <div class="preview" v-html="markedContent" v-if="isPreview"></div>
      </div>
      <!-- Bootstrap 按钮组-->
      <div class="btn-group btn-group-justified" role="group">
        <div class="btn-group" role="group">
          <!-- 后面会实现 markdown 支持，这是预览按钮 -->
          <button
            type="submit"
            class="btn btn-default"
            @click.prevent="isPreview=!isPreview"
          >
            {{ isPreview ? '继续编辑' : '预览' }}
          </button>
        </div>
        <div class="btn-group" role="group">
          <button type="submit" class="btn btn-default" @click.prevent="submit">
            发布
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
// 先导入
import marked from 'marked'


  export default {
    data() {
      return {
        isPreview: false,
         // 初始化创建帖子的 form，有三个必填字段
        form: new Form({
          title: '',
          content: '',
          topic_name: ''
        })
      }
    },
    computed: {
       // 方便使用
      topics() {
        return this.$store.state.topics
      },
      // 放在 computed 中
      markedContent() {
         // 直接调用 marked 函数可以了
         // 开启 sanitize 表示将 html 标签作为文本输出
         return marked(this.form.content, { sanitize: true })
      }
    },
   methods: {
      submit() {
        this.form.post('/api/posts')
          .then(data => {
            this.$store.commit('addPost', { post: data })
            this.$router.push('/')
          })
      },
   },
  }
</script>


<style>
  .post-form {
  margin-bottom: 15px;
}
.post-form input, textarea, select{
  width: 100%;
  padding: 10px 0px;
  border: none;
  outline: none;
}
.post-form select {
  height: 40px;
}
.post-form textarea {
  font-size: 18px;
  color: #454545;
}
.post-form .post-title {
  font-size: 36px;
  font-weight: 600px;
}
.post-form .post-topic {
  font-size: 12px;
}
</style>


