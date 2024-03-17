import requests, time, logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("log_file.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def ping(url):
    result = requests.get(url)
    method = result.request.method
    return (result.status_code == 200, method)

url = "http://ulm.illwinter.com/"

while True:
    try:
        isOnline, method = ping(url)
        if(isOnline == True):
            logger.info(f"[{time.strftime('%D')},   {time.strftime('%H:%M:%S')}] {method} {url} ulm is online")
        else:
            logger.info(f"[{time.strftime('%D')}, {time.strftime('%H:%M:%S')}] {method} {url} ulm is offline")
    except:
        logger.error(f"[{time.strftime('%D')}, {time.strftime('%H:%M:%S')}] unable to connect")
    time.sleep(2)