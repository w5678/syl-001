<template>
  <div class="post-view">
    <div class="yue container app__container">
      <div class="post-title" v-text="post.title"></div>
      <post-meta :post="post"></post-meta>
      <div class="post-content" v-html="markedContent"></div>
      <!-- 添加到 content 下面 -->
      <div class="post-actions">
        <button type="button" class="btn btn-success" aria-label="Left Align">
          <span class="glyphicon glyphicon-heart-empty" aria-hidden="true"></span
          >&nbsp;喜欢
        </button>
      </div>
    </div>
    <comment-box></comment-box>
  </div>
</template>

<script>
  import marked from 'marked'
  import PostMeta from '../components/PostMeta.vue'
  import CommentBox from '../components/CommentBox.vue'

  export default {
    data() {
      return {
      }
    },
    computed: {
       // 从所有的 posts 中获取到当前 id 的 post
      post() {
       return this.$store.state.posts.find(post => post.id == this.$route.params.id)
      },
      markedContent() {
        return marked(this.post.content, { sanitize: true })
      }
    },
    components:{
     PostMeta,
     CommentBox
    }
  }
</script>

<style>
  .post-view .post-title {
    font-size: 36px;
    font-weight: 600px;
  }
</style>



