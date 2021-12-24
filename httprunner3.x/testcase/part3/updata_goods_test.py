# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcase\part3\updata_goods.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseUpdataGoods(HttpRunner):

    config = (
        Config("用例描述-修改商品用例")
        .variables(
            **{
                "sp_id": 1,
                "goodsname": "yoyo",
                "goodscode": "sp_100861117",
                "merchantid": "10001",
                "merchantname": "悠悠学堂",
                "goodsprice": 99.9,
                "stock": 100,
                "goodsgroupid": 0,
                "goodsstatus": 1,
                "price": 21.0,
            }
        )
        .base_url("http://49.235.92.12:8201")
    )

    teststeps = [
        Step(
            RunRequest("修改商品")
            .put("/api/v1/goods/$sp_id")
            .with_json(
                {
                    "goodsname": "$goodsname",
                    "goodscode": "$goodscode",
                    "merchantid": "$merchantid",
                    "merchantname": "$merchantname",
                    "goodsprice": "$goodsprice",
                    "stock": "$stock",
                    "goodsgroupid": "$goodsgroupid",
                    "goodsstatus": "$goodsstatus",
                    "price": "$price",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "success!")
            .assert_equal(
                "body.data.goodsstatus", "${get_db_goods($sp_id, goodsstatus)}"
            )
        ),
    ]


if __name__ == "__main__":
    TestCaseUpdataGoods().test_start()