from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# =========================
# 📊 Prometheus 指标
# =========================
REQUEST_COUNT = Counter(
    'request_count',
    'Total request count of the app'
)

# =========================
# 🌐 主接口
# =========================
@app.route("/")
def hello():
    REQUEST_COUNT.inc()  # 每次访问 +1
    return "Hello CI/CD + Monitoring 🚀"

# =========================
# 📈 Prometheus 监控接口
# =========================
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# =========================
# 🚀 启动入口
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
