evaluates = [
    {'reduceUserNick': '用户A', 'feedback': '很好', 'feedbackDate': '2023-01-01'},
    {'reduceUserNick': '用户B', 'feedback': '一般', 'feedbackDate': '2023-01-02'}
]

for evaluate in evaluates:
    # It just like this "evaluate = {'reduceUserNick': '用户A', 'feedback': '很好', 'feedbackDate': '2023-01-01'}"
    dic = {
        '评论人': evaluate['reduceUserNick'],
        '评论内容': evaluate['feedback'],
        '评论时间': evaluate['feedbackDate'],
    }
    print(dic)