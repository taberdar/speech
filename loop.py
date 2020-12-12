#!/usr/bin/env python3

import smtplib

gmail_user = 'xx@gmail.com'
gmail_password = 'xx'

sent_from = gmail_user
to = ['recipient']
subject = "Swearing"
body = "Rude"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    #print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    #print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        #print("Say something!")
        with m as source: audio = r.listen(source)
        #print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            rude = value.find('*')
            if rude != -1:
                print("Rude")
                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(gmail_user, gmail_password)
                    server.sendmail(sent_from, to, email_text)
                    server.close()
                    print ("Email sent!")
                except:
                    print ('Something went wrong...')

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                #print(u"You said {}".format(value).encode("utf-8"))
                pass
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
                #pass
        except sr.UnknownValueError:
            pass
            #print("Oops! Didn't catch that")
        except sr.RequestError as e:
            pass
            #print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass