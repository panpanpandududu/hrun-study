# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\part3\upfile.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseUpfile(HttpRunner):

    config = Config("上传文件").base_url("http://49.235.92.12:8201")

    teststeps = [
        Step(
            RunRequest("step-上传文件")
            .post("/api/v1/upfile/")
            .upload(**{"file": "data/part_0.png", "title": "上海-悠悠"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "success!")
        ),
    ]


if __name__ == "__main__":
    TestCaseUpfile().test_start()