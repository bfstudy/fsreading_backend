

# 环境
## 本地dev环境
+ mac m1 pro
## 线上prod环境
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
1. mysql开始用的mysql镜像，但是在mac m系列芯片上有点问题，导入sql一直失败，换成mysql-server后才导入成功。
2. 创建apollo用户名和密码：
```shell
CREATE USER 'apollo'@'%' IDENTIFIED BY 'admin';
GRANT ALL ON *.* TO 'apollo'@'%';
```
3. 记得通过`docker inspect fs-apollo-config`查看config服务的IP地址，然后在configDB的serverconfig表中
修改eureka.service.url的localhost地址为config服务的IP地址。
