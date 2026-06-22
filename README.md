# 🚀 DevOps Full Stack Monitoring Project

基于 Docker Compose 搭建的完整 DevOps 监控系统，包含：

- Flask 应用（业务服务）
- Nginx（反向代理）
- Prometheus（监控采集）
- Grafana（可视化）
- Elasticsearch + Kibana + Logstash（日志系统）

---

# 🧱 架构图

```

Internet
│
│
▼
Nginx (80)
├── / → Flask App (5000)
├── /grafana → Grafana (3000)
└── /prometheus → Prometheus (9090)

````

---

# 🛠 技术栈

- Docker / Docker Compose
- Nginx
- Prometheus
- Grafana
- Flask (Python)
- Elasticsearch / Logstash / Kibana (ELK)
- Linux (Ubuntu Server)

---

# ⚙️ 一键启动

```bash
git clone https://github.com/你的用户名/devops-compose.git
cd devops-compose

docker-compose up -d --build
````

---

# 🌐 访问地址

| 服务         | 地址                                     |
| ---------- | -------------------------------------- |
| Flask App  | [http://IP](http://IP)                 |
| Grafana    | [http://IP/grafana](http://IP/grafana) |
| Prometheus | [http://IP:9090](http://IP:9090)       |
| Kibana     | [http://IP:5601](http://IP:5601)       |

---

# 📊 监控说明

## Prometheus

* 采集 Flask metrics
* 监控 CPU / 内存 / 请求数
* 默认端口：9090

访问：

```
http://IP:9090/targets
```

---

## Grafana

* 数据源：Prometheus
* 可视化监控指标
* 登录默认：admin / admin

---

## Flask Metrics 示例

```text
request_count_total
process_cpu_seconds_total
process_resident_memory_bytes
```

---

# 🚀 CI/CD（GitHub Actions 自动部署）

## 📁 文件结构

```
.github/workflows/deploy.yml
```

---

## ⚙️ deploy.yml

```yaml
name: Deploy to Server

on:
  push:
    branches: [ "main" ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Deploy to Server via SSH
      uses: appleboy/ssh-action@v1.0.3
      with:
        host: ${{ secrets.SERVER_IP }}
        username: root
        key: ${{ secrets.SSH_KEY }}
        script: |
          cd /root/devops-compose
          git pull origin main
          docker-compose down
          docker-compose up -d --build
```

---

# 🔐 GitHub Secrets 配置

在 GitHub：

```
Settings → Secrets and variables → Actions
```

添加：

| Key       | Value   |
| --------- | ------- |
| SERVER_IP | 你的服务器IP |
| SSH_KEY   | 你的私钥    |

---

# 🧠 工作流程

```
本地修改代码
   ↓
git push origin main
   ↓
GitHub Actions
   ↓
SSH 登录服务器
   ↓
git pull + docker-compose rebuild
   ↓
自动更新上线
```

---

# 📌 未来可扩展

* 🔥 Prometheus Alertmanager（告警）
* 🔥 Node Exporter（机器监控）
* 🔥 cAdvisor（容器监控）
* 🔥 HTTPS + 域名
* 🔥 Kubernetes 版本迁移

---

# 🏁 项目亮点

✔ 完整 DevOps 监控体系
✔ 可观测性（Observability）
✔ CI/CD 自动化部署
✔ 微服务 + 容器化
✔ 面试级项目

```

---

