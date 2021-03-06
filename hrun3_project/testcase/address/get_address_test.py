# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\address\get_address.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcase.login.login_success_test import TestCaseLoginSuccess as LoginSuccess


class TestCaseGetAddress(HttpRunner):

    config = (
        Config("查询收获地址")
        .variables(
            **{
                "tel": "15001234001",
                "name": "上海-悠悠",
                "address": "上海市徐汇区xx路1001号",
                "postal": "200000",
                "code": 0,
                "msg": "success!",
            }
        )
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(RunTestCase("step1-login").call(LoginSuccess).export(*["token"])),
        Step(
            RunRequest("step2-add address")
            .post("/api/v2/address")
            .with_headers(**{"Authorization": "Token $token"})
            .with_json(
                {
                    "tel": "$tel",
                    "name": "$name",
                    "address": "$address",
                    "postal": "$postal",
                }
            )
            .validate()
            .assert_equal("body.code", "$code")
            .assert_equal("body.msg", "$msg")
        ),
        Step(
            RunRequest("step3-get address")
            .get("/api/v2/address")
            .with_headers(**{"Authorization": "Token $token"})
            .validate()
            .assert_equal("body.code", "$code")
            .assert_equal("body.msg", "$msg")
            .assert_equal("body.data.tel", "$tel")
            .assert_equal("body.data.name", "$name")
            .assert_equal("body.data.address", "$address")
            .assert_equal("body.data.postal", "$postal")
        ),
    ]


if __name__ == "__main__":
    TestCaseGetAddress().test_start()
