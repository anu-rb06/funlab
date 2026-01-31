from flask import Flask, jsonify, request
import os
import time
import platform
import random
import socket

app = Flask(__name__)
START_TIME = time.time()

JOKES = [
    "Why do DevOps engineers love coffee? Because without it, deployments fail.",
    "I tried to fix a bug once… now it’s a feature.",
    "Kubernetes walked into a bar… bartender said: 'We don’t serve pods here.'",
    "Git told me to commit. I said I’m not ready for that kind of relationship.",
]

def uptime_seconds() -> int:
    return int(time.time() - START_TIME)

@app.get("/")
def home():
    return jsonify({
        "app": "Fun Python Docker Lab",
        "message": "Try /health, /joke, /info, /lucky?name=Satya, /echo",
        "uptime_seconds": uptime_seconds()
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok", "uptime_seconds": uptime_seconds()})

@app.get("/joke")
def joke():
    return jsonify({"joke": random.choice(JOKES)})

@app.get("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "env": {
            "APP_ENV": os.getenv("APP_ENV", "dev"),
            "APP_COLOR": os.getenv("APP_COLOR", "blue"),
        },
        "uptime_seconds": uptime_seconds()
    })

@app.get("/lucky")
def lucky():
    name = request.args.get("name", "friend")
    seed = sum(ord(c) for c in name)
    random.seed(seed + uptime_seconds() // 10)
    return jsonify({"name": name, "lucky_number": random.randint(1, 99)})

@app.post("/echo")
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify({
        "you_sent": data,
        "note": "Send JSON like {\"msg\":\"hello\"}"
    })

if __name__ == "__main__":
    # Important: host=0.0.0.0 so Docker can expose it
    app.run(host="0.0.0.0", port=8000)

