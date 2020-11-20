from flask import jsonify, session, request
from wetalk.models import Post,Topic
from . import api
from wetalk.forms import PostForm

@api.route('/posts', methods=['POST'])
def create_post():
    # 这个接口需要用户先登录
    if not session.get('id', ''):
        return jsonify(message='未登录'), 403
    form = PostForm.create_from_json()
    if not form.validate():
        return jsonify(form.errors), 422
    post = form.create_post()
    return jsonify(post.to_dict()), 201

#@api.route('/posts', methods=['GET'])
#def get_posts():
#    posts = Post.query.order_by(Post.created_at.desc())
#    return jsonify([post.to_dict() for post in posts])


#@api.route('/posts', methods=['GET'])
#def get_posts():
#    # 前端需要传 offset 过来
#    offset = request.args.get('offset', 0, type=int)
#    # 默认每次加载 10 个
#    limit = 2
#    q = Post.query.order_by(Post.created_at.desc())
#    # 使用 sqlalchemy 的 offset、limit 函数
#    posts = q.offset(offset).limit(limit)
#    data = [post.to_dict() for post in posts]
#    # 如果长度小于 limit，说明已经没有帖子了
#    if len(data) < limit:
#        offset = 0
#    else:
#        # 下次开始的位置
#        offset = offset + limit
#    # 返回 offset，前端下次加载只需要把这个值传过来
#    return jsonify(data=data, offset=offset)


@api.route('/posts', methods=['GET'])
def get_posts():
    print(request.args)
    offset = request.args.get('offset', 0, type=int)
    # 从参数获取传入的话题，默认全部话题
    topic = request.args.get('topic', '全部话题')
    # 改为一次加载 5 个了
    limit = 5
    q = Post.query
    if topic != '全部话题':
        # 如果话题存在，通过 topic_id 执行筛选
        topic = Topic.query.filter_by(name=topic).first()
        if topic:
            q = q.filter(Post.topic_id == topic.id)
    q = q.order_by(Post.created_at.desc())
    posts = q.offset(offset).limit(limit)
    data = [post.to_dict() for post in posts]
    if len(data) < limit:
        offset = 0
    else:
        offset = offset + limit
    return jsonify(data=data, offset=offset)

