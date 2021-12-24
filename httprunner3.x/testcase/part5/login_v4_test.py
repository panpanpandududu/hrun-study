from httprunner import HttpRunner, Config, Step, RunRequest


class TestLoginV4Case(HttpRunner):
    config = Config("登录v4用例").base_url("http://49.235.92.12:8201")
    teststeps = [
        Step(RunRequest("step-login")
             .post("/api/v4/login")
             .with_data({"username": "test", "password": "123456"})
             .validate()
             .assert_equal("status_code", 200)
             .assert_equal('headers.\"Content-Type\"', 'application/json')
             )
    ]