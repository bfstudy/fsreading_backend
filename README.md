

# 环境
## 本地开发环境
+ mac m1 pro
## 线上生产环境
+ Ubuntu 22.04 LTS
## python环境
3.10.14
## 包管理器
poetry
## 代码格式化工具
ruff
## 部署环境
docker compose
## 依赖中间件
+ apollo
+ mysql
+ redis

# 踩坑记录
## dev环境
1. mysql开始用的mysql镜像，但是在mac m芯片上有各种问题，导入sql一直失败，换成mysql-server后才导入成功。