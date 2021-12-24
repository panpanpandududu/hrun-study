from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestInfoCase(HttpRunner):
    config = (Config("用例的描述")
              .base_url("http://49.235.92.12:8201")
              .variables(**{"user": "test", "password": "123456"})
              .export(*["token"])
              )
    teststeps = [
        Step(
            RunRequest("step-login")
            .post("/api/v1/login")
            .with_json({"username": "$user", "password": "$password"})
            .extract()
            .with_jmespath('body.token', "token")
            .validate()
            .assert_equal('status_code', 200)
            .assert_equal('body.code', 0)
            .assert_equal('body.msg', 'login success!')
        ),
        Step(
            RunRequest("step2-info")
            .post('/api/v1/userinfo')
            .with_headers(**{"Authorization": "Token $token"})
            .with_json({"name": "$user",
                        "sex": "M",
                        "age": 20,
                        "mail": "283340479@qq.com"
                        })
            .validate()
            .assert_equal('status_code', 200)
            .assert_equal('body.code', 0)
            .assert_equal('body.message', 'update some data!')
        )
    ]