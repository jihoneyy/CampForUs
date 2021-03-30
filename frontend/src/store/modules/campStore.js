import axios from "axios";

<<<<<<< HEAD
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
=======
const SERVER_URL = process.env.VUE_APP_SERVER_URL
>>>>>>> b888fd488b9df6dd4220b9a0c47a886f2773d7d3

const campStore = {
  namespaced: true,

  state: {
    detailInfo: [],
    searchWordList: [],
    searchTagList: [[]]
  },
  getters: {
    getDetailInfo(state) {
      return state.detailInfo;
    },
    getSearchWordList(state) {
      console.log(state.searchWordList[0]);
      return state.searchWordList;
    },
    getSearchTagList(state) {
      return state.searchTagList;
    }
  },
  mutations: {
    setDetailInfo(state, payload) {
      state.detailInfo = payload;
    },
    setSearchWordList(state, payload) {
      state.searchWordList = payload;
    },
    setSearchTagList(state, payload) {
      state.searchTagList = payload;
    }
  },
  actions: {
    campsiteDetail(context, campsite_id) {
      axios({
        method: "get",
        url: `${SERVER_URL}/camp/getDetail/${campsite_id}`
      })
        .then(res => {
          console.log(res.data);
          context.commit("setDetailInfo", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
    searchByWord(context, word) {
      console.log("searchByWord");
      axios({
        method: "post",
        url: `${SERVER_URL}/camp/getwordresult/`,
        data: {
          word: word
        }
      })
        .then(res => {
          console.log(res.data);
          context.commit("setSearchWordList", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    },

    searchByTag(context, tagList) {
      axios({
        method: "post",
        url: `${SERVER_URL}/camp/gettagresult/`,
        data: tagList
      })
        .then(res => {
          console.log(res);
          context.commit("setSearchTagList", res.data);
          //context.commit("searchTagList", tagList);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
export default campStore;
