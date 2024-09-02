# pytest-send-email


Plugin to send email after pytest execution with results.

[![PyPI version](https://badge.fury.io/py/pytest-send-email.svg)](https://badge.fury.io/py/pytest-send-email)
[![Downloads](https://pepy.tech/badge/pytest-send-email)](https://pepy.tech/project/pytest-send-email)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)]()
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]()
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)]()

---

### How it works:

- Get execution details using  `pytest_terminal_summary()` hook
- Build html template
- Send's email for respective recipients

---

### How to use in project:

1. Install `pytest-send-email`

> Case 1: Using `setup.py` (clone repo and run command in root)
```
python setup.py install
```

> Case 2: Install from Pypi
```
pip install pytest-send-email
```

2. Execute test's normally using options
Add SMTP_HOST, SMTP_USER,SMTP_PWD to ENV
```
export SMTP_HOST=<smtp-server>
export SMTP_USER=<your-email-user>
export SMTP_PWD=<your-password>
```
If you need smtp ssl or customize smtp port, add SMTP_PORT or SMTP_SSL to ENV
```
export SMTP_PORT=465
export SMTP_SSL=True
```
And run pytest with options `--send-email` and `--email-receivers=<email_addr>,<email_addr>`
```
pytest --send-email --email-receivers=abc@gmail.com,abc@hotmail.com
```

You can also config email receivers, subject, body and smtp info in pytest.ini
```
[pytest]
addopts = --send-email --html=report.html

smtp_host = <smtp-server>
smtp_port = <smtp-port>
smtp_user = <your-email-user>
smtp_pwd = <your-password or token>
smtp_ssl = False


email_receivers = superhin@126.com
email_subject = Pytest Test Report
email_body = 
    Hi, this is the test report
email_attachments=test_a.py,report.html
```

Or you can config in pytest.ini with `[email]` section

```ini
addopts = --send-email --html=report.html

[email]
host = <smtp-server>
port = <smtp-port>
user = <your-email-user>
password = <your-password or token>
ssl = False

receivers = superhin@126.com
subject = Pytest Test Report
body = 
    Hi, this is the test report
attachments=test_a.py,report.html

```


Email options:
- --send-email: Send email when --send-email
- --email-receivers: Email receivers, comma-separated
- --smtp-host: SMTP host
- --smtp-port: SMTP port
- --smtp-user: SMTP user
- --smtp-pwd: SMTP password
- --smtp-ssl: Use smtp_ssl
- --email-subject: Email subject
- --email-body: Email content, support HTML
- --email-template: Email content template path
- --email-attachments: Email attachments, commn-separated

Email ini-options:

- --smtp_host: SMTP host
- --smtp_port: SMTP port
- --smtp_user: SMTP user
- --smtp_pwd: SMTP password
- --smtp_ssl: Use smtp_ssl
- --email_subject: Email subject
- --email_body: Email content, support HTML
- --email_receivers: Email receivers, comma-separated
- --email_template: Email content template path
- --email_attachments: Email attachments, commn-separated

> At least --send-email and --email-receivers or email_recervers are necessary
---

*Sample Report*

<img src="pytest_email.png" alt="pytest_email.png">

---

### What kind of information is shared?

Following test counts:
- Total
- Passed
- Failed
- Skipped
- Error
- XPassed
- XFailed
- Duration

Future: Failed test information

---

*Thanks for using pytest-send-email!*

If you have any questions / suggestions / comments on this, please feel free to reach me at

- Email: <a href="mailto:superhin@126.com?Subject=Pytest%20Email" target="_blank">`superhin@126.com`</a> 
- Blog: <a href="https://www.cnblogs.com/superhin/" target="_blank">`hanzhichao`</a>
- Jianshu: <a href="https://www.jianshu.com/u/0115903ded22" target="_blank">`hanzhichao`</a>

---
