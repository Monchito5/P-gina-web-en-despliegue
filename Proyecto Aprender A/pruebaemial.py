import smtplib
import os
#Variables
PASSWORD_APP = os.environ.get('EMAIL_APP_PASS')
EMAIL_APP = os.environ.get('EMAIL_USER')
#Conexión con el servidor
conexion = smtplib.SMTP(host= 'smtp.gmail.com', port= 587)
conexion.ehlo()
#Ecriptación TLS
conexion.starttls
#Conexión Login
conexion.login(user= EMAIL_APP, password= PASSWORD_APP)
#Enviar correo
mensaje = "Subject: Prueba 1\nEsto es una prueba"
conexion.sendmail(from_addr= EMAIL_APP, to_addrs= EMAIL_APP, msg= mensaje) 
#Fin
conexion.quit()