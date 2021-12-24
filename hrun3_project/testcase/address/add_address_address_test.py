# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\address\add_address_address.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcase.login.login_success_test import TestCaseLoginSuccess as LoginSuccess


class TestCaseAddAddressAddress(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "address-code-msg": [
                    [None, 0, "success!"],
                    ["", 0, "success!"],
                    [12345, 0, "success!"],
                    ["上海市徐汇区xx 路 1001 号101", 0, "success!"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("添加收获地址")
        .variables(
            **{
                "tel": 15001234001,
                "name": "上海-悠悠",
                "address": "上海市徐汇区xx路1001号",
                "postal": 200000,
                "code": 0,
                "msg": "success!",
            }
        )
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(RunTestCase("step1-login").call(LoginSuccess).export(*["token"])),
        Step(
            RunRequest("step2-添加收获地址")
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
    ]


if __name__ == "__main__":
    TestCaseAddAddressAddress().test_start()