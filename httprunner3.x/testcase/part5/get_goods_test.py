from httprunner import HttpRunner, Config, Step, RunRequest


class TestGetGoodsCase(HttpRunner):
    config = Config("查询全部商品").base_url("http://49.235.92.12:8201")

    teststeps = [
        Step(
            RunRequest("step-get goods")
            .get("/api/v1/goods")
            .with_params(**{"page": 1, "size": 2})
            .validate()
            .assert_equal('body.code', 0)
            .assert_equal('body.msg', 'success!')
        )
    ]