from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestLoginCase(HttpRunner):
    config = (Config("用例的描述")
              .base_url("http://49.235.92.12:8201")
              .variables(**{"user": "test", "password": "123456"})
              .export(*["token"])
              )
    teststeps = [
        Step(
            RunRequest("step-login")
            .post("/api/v4/login")
            .with_data({"username": "$user", "password": "$password"})
            .extract()
            .with_jmespath('body.token', "token")
            .validate()
            .assert_equal('status_code', 200)
            .assert_equal('body.code', 0)
            .assert_equal('body.msg', 'login success!')
        )
    ]


