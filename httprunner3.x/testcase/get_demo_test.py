# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\get_demo.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseGetDemo(HttpRunner):

    config = Config("demo case")

    teststeps = [
        Step(
            RunRequest("step-demo")
            .get("http://49.235.92.12:8201/api/test/demo")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "成功success!")
        ),
    ]


if __name__ == "__main__":
    TestCaseGetDemo().test_start()
