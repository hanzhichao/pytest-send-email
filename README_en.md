# pytest-send-eemail


Plugin to send email after pytest execution with results.

[![PyPI version](https://badge.fury.io/py/pytest-email.svg)](https://badge.fury.io/py/pytest-email)
[![Downloads](https://pepy.tech/badge/pytest-email)](https://pepy.tech/project/pytest-email)
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

> Case 2: Install from git (changes in master)
```
pip install git+https://github.com/hanzhichao/pytest-send-email
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
email_receivers = superhin@126.com,hanzhichao@secoo.com
email_subject = Pytest Report
email_attachments=test_a.py,report.html
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

*Thanks for using pytest-email!*

If you have any questions / suggestions / comments on this, please feel free to reach me at

- Email: <a href="mailto:superhin@126.com?Subject=Pytest%20Email" target="_blank">`superhin@126.com`</a> 
- Blog: <a href="https://www.cnblogs.com/superhin/" target="_blank">`hanzhichao`</a>
- Jianshu: <a href="https://www.jianshu.com/u/0115903ded22" target="_blank">`hanzhichao`</a>

---
