"""
查询所有用户数据
User.query.all()
查询1号用户  只能填id
User.query.get(1)
#查询所有用户数据
User.query.all()
#查询有多少个用户
User.query.count()
#查询第1个用户
User.query.first()
#查询id为4的用户[3种方式]
User.query.get(4)
# filter_by精确查询
User.query.filter_by(id=4).first()
# filter全局过滤查询，必须指明id是来源于那张表
User.query.filter(User.id==4).first()
#查询名字以`张`开头的所有数据[startswith开始/endswith结尾/contains包含]
User.query.filter(User.name.startswith('张'))
# 查询手机号码为 18516952650 同时  名字以 `号` 结尾的
User.query.filter(User.name.endswith('号'), User.mobile=='18516952650').first()
# 查询手机号码为 13021074747 或者  名字以 `号` 结尾的
User.query.filter(or_(User.name.endswith('号'), User.mobile=='13021074747')).all()
# 查询手机号码不是为 13911111111  --- 非
User.query.filter(User.mobile!='13911111111').all()
# offset 偏移，起始位置
# 只取前三条数据  limit 获取限制数据
User.query.offset(3).all()
# 根据id排序  order_by 排序
User.query.order_by(User.id.desc()).all()

"""
