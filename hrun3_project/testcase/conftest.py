import pytest

# 数据准备
# 1.登录依赖
"""
登录账号 test 123456
"""
# 2.商品
"""
删除/查询商品  需保证sp_id=123456不存在
修改商品
需保证sp_id=1存在，并且goodscode=sp_test1
sp_10086在数据库中存在
"""
from utils.connect_mysql import DbConnect, dbinfo


@pytest.fixture(scope="session", autouse=True)
def before_run():
    """用例前执行数据准备SQL"""
    print("准备测试数据，用例依赖的数据，先在数据库造好")
    db = DbConnect(dbinfo, database="apps")
    # 1.删除商品id=123456的数据
    sql1 = "DELETE from apiapp_goods WHERE id = '123456'"
    db.execute(sql1)
    # 查询商品id=1的是否存在
    sql2 = "SELECT id,  goodscode from apiapp_goods where id=1"
    sql3 = "INSERT INTO `apps`.`apiapp_goods` (`id`, `merchantid`, `goodsname`, `goodsprice`, `stock`, `goodsgroupid`, `goodsstatus`, `price`, `create_time`, `merchantname`, `goodscode`, `update_time`) VALUES ('1', '10001', 'yoyo123', '99.9', '100', '0', '1', '21', '2021-05-07 16:35:07.648610', '悠悠学堂', 'sp_test1', '2021-08-20 16:32:35.209975');"
    sql4 = "DELETE from apiapp_goods WHERE goodscode = 'sp_test1'"
    res1 = db.select(sql2)
    print(res1)
    if len(res1) == 0:
        # 如果不存在，执行sql写一个数据
        # 保证sp_id=1存在，并且goodscode=sp_test1
        # goodscode在数据库要是唯一的，可以先删除，再插入数据
        db.execute(sql4)
        db.execute(sql3)
    db.close()



