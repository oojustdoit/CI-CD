# 🚀 CI/CD DevOps Demo Project

一个基于 **Flask + Docker + Nginx + Gunicorn + GitHub Actions** 构建的完整 CI/CD 自动化部署项目。

该项目实现了从代码提交 → 自动构建 → 自动部署 → 服务更新的完整 DevOps 流水线。

---

# 📌 项目架构

本项目采用典型的生产级 Web 架构：

```

浏览器
↓
Nginx（反向代理）
↓
Gunicorn（WSGI服务器）
↓
Flask（业务应用）
↓
Docker（容器化运行）

````

---

# 🧱 技术栈

- Python 3.10
- Flask
- Gunicorn
- Docker
- Docker Compose
- Nginx
- GitHub Actions（CI/CD）
- SSH 自动化部署

---

# 🚀 核心功能

## ✔ Web 服务
- 基于 Flask 构建轻量 Web 服务
- 提供 HTTP API 响应

## ✔ 容器化部署
- 使用 Docker 构建运行环境
- Docker Compose 一键启动多服务

## ✔ 反向代理
- Nginx 作为统一入口
- 转发请求到 Flask 服务

## ✔ 生产级 WSGI
- 使用 Gunicorn 多进程部署 Flask
- 提升并发能力与稳定性

## ✔ CI/CD 自动化部署
- GitHub Actions 自动触发部署
- SSH 自动登录服务器
- 自动执行：
  - git pull
  - docker-compose rebuild
  - 服务自动更新

---

# 📂 项目结构

```

devops-compose/
├── app/
│   ├── app.py               # Flask 应用
│   └── requirements.txt     # Python依赖
│
├── nginx/
│   └── default.conf        # Nginx配置
│
├── Dockerfile              # Flask镜像构建
├── docker-compose.yml      # 服务编排
│
├── .github/
│   └── workflows/
│       └── deploy.yml      # CI/CD自动部署流程
│
├── certbot/                # HTTPS证书（预留）
└── letsencrypt/            # HTTPS支持目录

````

---

# ⚙️ 本地运行方式

## 1️⃣ 克隆项目

```bash
git clone https://github.com/oojustdoit/CI-CD.git
cd CI-CD
```

---

## 2️⃣ 构建并启动

```bash
docker-compose up -d --build
```

---

## 3️⃣ 访问服务

```
http://localhost
```

---

# 🚀 CI/CD 自动部署流程

本项目使用 GitHub Actions 实现自动部署：

## 🔁 流程如下：

```text
代码 push 到 main 分支
        ↓
GitHub Actions 自动触发
        ↓
SSH 登录云服务器
        ↓
拉取最新代码 (git pull)
        ↓
重新构建 Docker
        ↓
自动重启服务
        ↓
部署完成
```

---

## 📄 GitHub Actions 配置

核心文件：

```
.github/workflows/deploy.yml
```

---

## ⚙️ 部署步骤（自动执行）

服务器执行：

```bash
git pull origin main
docker-compose down
docker-compose up -d --build
```

---

# 🔐 环境变量（GitHub Secrets）

本项目依赖以下 Secrets：

| Key     | 说明             |
| ------- | -------------- |
| HOST    | 云服务器 IP        |
| SSH_KEY | SSH 私钥（用于免密登录） |

---

# 🧠 架构说明

## 🟢 为什么使用 Gunicorn？

* Flask 自带服务器不适合生产
* Gunicorn 支持多进程
* 提升并发能力

---

## 🟢 为什么使用 Nginx？

* 作为统一入口
* 处理反向代理
* 支持负载均衡扩展

---

## 🟢 为什么用 Docker？

* 环境一致性
* 一键部署
* 易于扩展

---

# 📈 项目亮点

* ✅ 完整 CI/CD 自动化流水线
* ✅ 云服务器自动部署
* ✅ Docker 容器化架构
* ✅ 生产级 Web 服务结构
* ✅ 可扩展为微服务架构

---

# 🧪 测试方式

修改代码：

```python
return "CI/CD SUCCESS 🚀"
```

提交：

```bash
git add .
git commit -m "test ci/cd"
git push
```

自动触发部署，无需手动操作。

---

# 🚀 未来可扩展方向

* Kubernetes 集群部署
* Jenkins 流水线升级
* Prometheus + Grafana 监控
* ELK 日志系统
* 蓝绿部署 / 灰度发布
* 多环境（dev / test / prod）
