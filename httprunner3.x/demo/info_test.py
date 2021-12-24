from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcase.part5.login_v1 import TestLoginCase


class TestUserInfoCase(HttpRunner):

    config = Config("case").base_url("http://49.235.92.12:8201")

    teststeps = [
        Step(RunTestCase("step1-login")
             .call(TestLoginCase)
             .export(*["token"])),
        Step(RunRequest("step2-info")
             .get("/api/v1/userinfo")
             .with_headers(**{"Authorization": "Token $token"})
             .validate()
             .assert_equal("body.code", 0))
    ]