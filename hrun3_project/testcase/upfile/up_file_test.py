# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\upfile\up_file.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseUpFile(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "filename-titlename-code-msg": [
                    ["data/hrun3.png", "上海-悠悠", 0, "success!"],
                    ["data/hrun3.jpg", "上海-悠悠", 0, "success!"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("文件上传").base_url("${ENV(base_url)}")

    teststeps = [
        Step(
            RunRequest("文件上传")
            .post("/api/v1/upfile/")
            .upload(**{"file": "$filename", "title": "$titlename"})
            .validate()
            .assert_equal("body.code", "$code")
            .assert_equal("body.msg", "$msg")
        ),
    ]


if __name__ == "__main__":
    TestCaseUpFile().test_start()