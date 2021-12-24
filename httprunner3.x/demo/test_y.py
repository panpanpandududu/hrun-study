from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLogin(HttpRunner):

    config = (
        Config("用例描述-登录用例")
        .variables(**{"user": "${ENV(user)}", "psw": "${ENV(psw)}"})
        .base_url("${ENV(base_url)}")
        .export(*["token"])
    )

    teststeps = [
        Step(
            RunRequest("step-登录")
            .post("/api/v1/login")
            .with_json({"username": "${ENV(user)}", "password": "${ENV(psw)}"})
            .extract()
            .with_jmespath("body.token", "token")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.msg", "login success!")
            .assert_equal("body.code", 0)
        )
    ]


if __name__ == "__main__":
    TestCaseLogin().test_start()
