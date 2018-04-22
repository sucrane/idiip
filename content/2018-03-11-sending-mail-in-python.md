Title: Sending Mail in Python
Date: 2018-03-11

We need to send mails sometimes, e.g. report sending service. `email`
module in Python will work this for us.

```python
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_mail(server, port, account, password, send_from, send_to,
              subject, text, files=None):
    """ Send mail in Python. """

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.starttls()
    smtp.login(account, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
```