import moment from "moment";

// 显示中文
moment.locale("zh-cn");

export function fromNow(time) {
  return moment(time).fromNow();
}


