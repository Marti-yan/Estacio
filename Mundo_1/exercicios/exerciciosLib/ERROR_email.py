import smtplib
import email.message
def enviar_email():
    corpo_email= """
    <p> 0lá yan </p>
    <p> Segue meu email automático </p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = "yanloufraga@gmail.com"
    msg['To'] = "martiyan2020@gmail.com"
    password = 'juxkbybjoiyxhovz'
    msg.add_header("Content-Type",'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP ('smtp.gmail.com: 587')
    s.starttis()
    #Login Credentials for sending the mail
    s.login(msg['From'],password)
    s.sendmall(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print('Email enviado')



