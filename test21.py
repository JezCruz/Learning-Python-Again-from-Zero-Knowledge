# Request - send msg using ntfy.sh

import requests
import time


me = "☺️"
msg = "Wassup!"
for i in range(100):
    requests.post("https://ntfy.sh/testmsg", data=(msg)[i % len(msg)])
    print(f"Sent message {i+1}/100")
    time.sleep(0.1)