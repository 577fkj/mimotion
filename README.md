# Mimotion
# 请不要点自己项目的 Create pull request 不要提起无意义的pr，否则你将会被我拉黑！
# 请不要点自己项目的 Create pull request 不要提起无意义的pr，否则你将会被我拉黑！
# 请不要点自己项目的 Create pull request 不要提起无意义的pr，否则你将会被我拉黑！
# 小米运动自动刷步数

> 小米运动自动刷步数

## Github Actions 部署指南

### 一、Fork 此仓库

### 二、设置账号密码
> 前往: Settings-->Secrets-->Actions-->New repository secret

> 依次添加名为: **PMODE**、**PKEY**、**USER**、**PWD**、**STEP**

#### 例如

![image](https://user-images.githubusercontent.com/86393520/180457841-4735aa49-6def-4c6f-92ad-f93235c505dc.png)

#### 参数详解

| Secrets |  格式  |
| -------- | ----- |
| PMODE |   推送模式,server酱推送:`wx` 新server酱推送:`nwx` tg推送:`tg` 企业微信推送:`qwx` PushPlus推送:`pp` 关闭推送:`off`|
| PKEY |   推送key,详见PKEY参数解释|
| USER |   账号,仅支持手机号|
| PWD |   密码|
| STEP |   步数:0则为1w-2w之间随机,自定义随机范围: `18000-25000`|

| PKEY参数解释 |  格式  |
| -------- | ----- |
| TG推送 |   `token@userid`|
| Server酱推送 |   `填写server酱的推送key`|
| 企业微信推送 |   `推送用户（可@all）-corpid-corpsecret-(agentid 空则为默认1000002)`|
| PushPlus推送 |   `token`|
| 关闭推送 |   `off`|

### 三、多账户(用不上请忽略)

多账户请用 **#** 分割 然后保存到变量 **USER** 和 **PWD**

#### 例如

**13800138000#13800138001** 变量 **USER**

**abc123qwe#abcqwe2** 变量 **PWD**

### 四、自定义启动时间

编辑 **.github/workflows/run.yml**

找到 cron: 0 10 * * *

修改其中的10为你要的时间

需要运行的时间-8就是UTC时间

## 注意事项

1. 每天运行一次，在下午 6 点

2. 多账户的数量和密码请一定要对上 不然无法使用!!!

3. 启动时间得是UTC时间!

4. server酱注册地址 [点我](https://sct.ftqq.com/)

5. 如果支付宝没有更新步数,到小米运动->设置->账号->注销账号->清空数据,然后重新登录,重新绑定第三方

6. 小米运动不会更新步数，只有关联的会同步！！！！！

7. 请各位在使用时Fork[主分支](https://github.com/577fkj/mimotion/)，防止出现不必要的bug.

8. TG推送教程 [点我](./TG_PUSH.md)

9. 请注意，账号不是 [小米账号]，而是 [小米运动] 的账号。

## 纪念一下往日的辉煌

[![](https://i.loli.net/2021/11/19/BLi5cpjPSxh7Am2.png)](https://i.loli.net/2021/11/19/BLi5cpjPSxh7Am2.png)

## 历史Star数

[![Stargazers over time](https://starchart.cc/577fkj/mimotion.svg)](https://starchart.cc/577fkj/mimotion)
