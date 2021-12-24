from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestLoginCase(HttpRunner):
    config = (
        Config("登录用例")
        .base_url("http://49.235.92.12:8201")
        .variables(user="test", psw="123456")
        .export(*["token"])
    )

    teststeps = [Step(
        RunRequest("step-login")
        .post("/api/v1/login")
        .with_json({"username": "${user}", "password": "${psw}"})
        .extract()
        .with_jmespath("body.token", "token")
        .validate()
        .assert_equal("body.code", 0, message="code不对")
    )]
