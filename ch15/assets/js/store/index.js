import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  me: {},
  loginForm: false,
  topics:[],
  posts:[],
  offset: 0,
  currentTopic: '全部话题'

}

const getters = {

}

const mutations = {
  showLoginForm: state => state.loginForm = true,
  hideLoginForm: state => state.loginForm = false,
  recordMe: (state, { me }) => state.me = me,
  setTopics: (state, { topics }) => (state.topics = topics),
  // 点击加载更多的时候，获取到 posts 需要需要添加到已经存在的列表末位
  addPosts: (state, { posts }) => state.posts = state.posts.concat(posts),
  // 因为帖子列表按时间排序，新创建的帖子添加到第一个位置
  addPost: (state, { post }) => state.posts.unshift(post),
  // set offset
  setOffset: (state, { offset }) => state.offset = offset,
  setCurrentTopic: (state, { topic }) => state.currentTopic = topic,
  // store/index.js
  clearPosts: (state) => (state.posts = []),

}

const actions = {
  loadPosts: ({ state, commit }) => {
    http
      .get("/api/posts", {
        params: { offset: state.offset, topic: state.currentTopic },
      })
      .then(({ data }) => {
        commit("addPosts", { posts: data.data });
        commit("setOffset", { offset: data.offset });
      });
    },
    // 传入选择的话题名称
    selectTopic: ({ state, commit, dispatch }, { topicName }) => {
      // 从头开始加载
      commit('setOffset', { offset: 0 })
      // 更新当前的话题
      commit('setCurrentTopic', { topic: topicName })
       // 清空帖子列表
      commit('clearPosts')
      // 调用 loadPosts action，执行加载
      dispatch('loadPosts')
    }
};

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
