# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\login.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLogin(HttpRunner):

    config = Config("用例描述-登录用例").export(*["token"])

    teststeps = [
        Step(
            RunRequest("step-登录")
            .post("http://49.235.92.12:8201/api/v1/login")
            .with_json({"username": "test", "password": "123456"})
            .extract()
            .with_jmespath("body.token", "token")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.msg", "login success!")
            .assert_equal("body.code", 0)
            .assert_equal("body.username", "test")
            .assert_length_equal("body.token", 40)
        ),
    ]


if __name__ == "__main__":
    TestCaseLogin().test_start()
