import os
import smtplib
from configparser import ConfigParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

DEFAULT_EMAIL_SUBJECT = 'Pytest Email Report'
DEFAULT_EMAIL_BODY_TPL = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <title>Pytest Email Report</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0 " />
        <style>
            .rf-box {
                max-width: 60%%;
                margin: auto;
                padding: 30px;
                border: 3px solid #eee;
                box-shadow: 0 0 10px rgba(0, 0, 0, .15);
                font-size: 16px;
                line-height: 28px;
                font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
                color: #555;
            }

            .rf-box table {
                width: 100%%;
                line-height: inherit;
                text-align: left;
            }

            .rf-box table td {
                padding: 5px;
                vertical-align: top;
                width: 50%%;
                text-align: center;
            }

            .rf-box table tr.heading td {
                background: #eee;
                border-bottom: 1px solid #ddd;
                font-weight: bold;
                text-align: left;
            }

            .rf-box table tr.item td {
                border-bottom: 1px solid #eee;
            }
        </style>
    </head>
    <body>
        <div class="rf-box">
            <table cellpadding="0" cellspacing="0">
                <tr class="top">
                    <td colspan="2">
                        <table>
                            <tr>
                                <td></td>
                                <td style="text-align:middle">
                                    <h1>%s</h1>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            <p style="padding-left:20px">
                Hi Team,<br>
                Following are the last pytest execution result.
            </p>
            <table style="width:80%%;padding-left:20px">
                <tr class="heading">
                    <td>Test Status</td>
                    <td>Number</td>
                </tr>
                <tr class="item">
                    <td>Total</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>Pass</td>
                    <td style="color:green">%s</td>
                </tr>
                <tr class="item">
                    <td>Fail</td>
                    <td style="color:red">%s</td>
                </tr>
                <tr class="item">
                    <td>Skip</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>Error</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>xPassed</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>xFailed</td>
                    <td>%s</td>
                </tr>
            </table>
        </div>
    </body>
</html>'''


def pytest_addoption(parser):
    group = parser.getgroup('email')
    group.addoption("--send-email", action="store_true", help="Send email when --send-email")
    group.addoption('--smtp-host', help='SMTP host')
    group.addoption('--smtp-port', help='SMTP port')
    group.addoption('--smtp-user', help='SMTP user')
    group.addoption('--smtp-pwd', help='SMTP password')
    group.addoption("--smtp-ssl", help="Use smtp_ssl")

    group.addoption('--email-subject', help='Email subject')
    group.addoption('--email-receivers', help='Email receivers, comma-separated')
    group.addoption('--email-body', help='Email content, support HTML')
    group.addoption('--email-template', help='Email content template path')
    group.addoption('--email-attachments', help='Email attachments, commn-separated')

    parser.addini('smtp_host', help='SMTP host')
    parser.addini('smtp_port', help='SMTP port')
    parser.addini('smtp_user', help='SMTP user')
    parser.addini('smtp_pwd', help='SMTP password')
    parser.addini('smtp_ssl', help="Use SMTP_SSL")

    parser.addini('email_subject', help='Email subject')
    parser.addini('email_receivers', help='Email receivers, comma-separated')
    parser.addini('email_body', help='Email content, support html')
    parser.addini('email_template', help='Email content template path')
    parser.addini('email_attachments', help='Email attachments, commn-separated')


def pytest_terminal_summary(terminalreporter, config):
    passed = len(terminalreporter.stats.get('passed', ""))
    failed = len(terminalreporter.stats.get('failed', ""))
    skipped = len(terminalreporter.stats.get('skipped', ""))
    error = len(terminalreporter.stats.get('error', ""))
    xpassed = len(terminalreporter.stats.get('xpassed', ""))
    xfailed = len(terminalreporter.stats.get('xfailed', ""))
    total = passed + failed + skipped + error + xfailed + xpassed

    if config.getoption("--send-email") is True:
        ini = ConfigParser(allow_no_value=True)
        ini.read(config.inifile)

        smtp_host = smtp_port = smtp_user = smtp_pwd = smtp_ssl = None
        email_subject = email_receivers = email_body = email_template = email_attachments = None
        if ini.has_section('email'):
            if ini.has_option('email', 'host'):
                smtp_host = ini.get('email', 'host')
            if ini.has_option('email', 'port'):
                smtp_port = ini.get('email', 'port')
            if ini.has_option('email', 'user'):
                smtp_user = ini.get('email', 'user')
            if ini.has_option('email', 'pwd'):
                smtp_pwd = ini.get('email', 'pwd')
            if ini.has_option('email', 'ssl'):
                smtp_ssl = ini.get('email', 'ssl')
            if ini.has_option('email', 'subject'):
                email_subject = ini.get('email', 'subject')
            if ini.has_option('email', 'receivers'):
                email_receivers = ini.get('email', 'receivers')
            if ini.has_option('email', 'body'):
                email_body = ini.get('email', 'body')
            if ini.has_option('email', 'template'):
                email_template = ini.get('email', 'template')
            if ini.has_option('email', 'attachments'):
                email_attachments = ini.get('email', 'attachments')

        smtp_host = config.getoption('--smtp-host') or config.getini('smtp_host') or smtp_host
        smtp_port = config.getoption('--smtp-port') or config.getini('smtp_port') or smtp_port
        smtp_user = config.getoption('--smtp-user') or config.getini('smtp_user') or smtp_user
        smtp_pwd = config.getoption('--smtp-pwd') or config.getini('smtp_pwd') or smtp_pwd
        smtp_ssl = config.getoption('--smtp-ssl') or config.getini('smtp_ssl') or smtp_ssl

        subject = config.getoption('--email-subject') or config.getini(
            'email_subject') or email_subject or DEFAULT_EMAIL_SUBJECT
        receivers = config.getoption('--email-receivers') or config.getini('email_receivers') or email_receivers

        body = config.getoption('--email-body') or config.getini('email_body') or email_body or DEFAULT_EMAIL_BODY_TPL
        template = config.getoption('--email-template') or config.getini('email_template') or email_template

        if template and isinstance(template, str) and os.path.isfile(template):
            try:
                with open(template, encoding='utf-8') as f:
                    body = f.read()
            except Exception as ex:
                logging.exception(ex)
        body = body % (subject, total, passed, failed, skipped, error, xpassed, xfailed)

        attachments = config.getoption('--email-attachments') or config.getini('email_attachments') or email_attachments

        if receivers:
            receivers = receivers.split(',')

        if attachments:
            attachments = attachments.split(',')

        send_email(subject, body, receivers, attachments,
                   smtp_host=smtp_host, smtp_port=smtp_port, smtp_user=smtp_user, smtp_pwd=smtp_pwd, smtp_ssl=smtp_ssl)


def send_email(subject, body, receivers, attachments=None, **kwargs):
    smtp_host = kwargs.get('smtp_host') or os.getenv('SMTP_HOST')
    smtp_port = kwargs.get('smtp_port') or os.getenv('SMTP_PORT')
    smtp_user = kwargs.get('smtp_user') or os.getenv('SMTP_USER')
    smtp_pwd = kwargs.get('smtp_pwd') or os.getenv('SMTP_PWD')
    smtp_ssl = kwargs.get('smtp_ssl') or os.getenv('SMTP_SSL')

    if not all([smtp_host, smtp_user, smtp_pwd]):
        logging.warning('Send no email for missing smtp_host,smtp_user or smtp_pwd')
        return

    if isinstance(receivers, str):
        receivers = receivers.split(',')

    if smtp_port and isinstance(smtp_port, str):
        try:
            smtp_port = int(smtp_port)
        except Exception as ex:
            logging.exception(ex)
            smtp_port = None

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = ','.join(receivers)

    msg.attach(MIMEText(body, 'html', 'utf-8'))

    if attachments:
        if isinstance(attachments, str):
            attachments = [attachments]
        for file_path in attachments:
            if os.path.isfile(file_path):
                try:
                    att = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
                except Exception as ex:
                    logging.exception(ex)
                else:
                    att['Content-Type'] = 'application/octet-stream'
                    att["Content-Disposition"] = f'attachment; filename={os.path.basename(file_path)}'
                    msg.attach(att)
    try:
        server = smtplib.SMTP_SSL(smtp_host, smtp_port) if smtp_ssl else smtplib.SMTP(smtp_host, smtp_port)
        server.login(smtp_user, smtp_pwd)
        server.sendmail(smtp_user, receivers, msg.as_string())
        print("Send email to %s done!" % ','.join(receivers))
    except Exception as ex:
        logging.exception(ex)
