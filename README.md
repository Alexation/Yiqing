<p align="center">
  <img src="http://47.108.208.140:8002/i/2022/02/14/p5q7iz.png" height="300" />
</p>

<span id="nav-2"></span>

## 内容目录

<details>
  <summary>点我 打开/关闭 目录列表</summary>

- [内容介绍](#nav-2)
- [项目介绍](#nav-3)
  - [项目网站](#nav-3-1)
  - [背景](#nav-3-2)
- [相关项目演示](#nav-4)
- [功能特色](#nav-5)
- [架构](#nav-6)

</details>

<span id="nav-3"></span>

## 项目介绍

项目名称：CTGU自动安全上报

所使用技术栈：Vue2 + Flask + MySQL

实现过程：用户通过提交表单数据到Flask提供的API接口，将学号密码存储到MySQL数据库中，再通过服务器端Python脚本每天调用数据库参数对CTGU安全上报接口进行请求，达到自动安全上报的要求。

<span id="nav-3-1"></span>

### 项目网站

[项目地址](http://47.108.208.140)

<span id="nav-3-2"></span>

### 背景

自动化程序可以帮助我们完成很多重复性的工作，小到每天签到打卡、人工输入数据，大到部分工程的检修、计算项目参数等工作渐渐地被计算机程序所替代，本项目的初心不仅仅是自动安全上报，更希望使用者能够合理地分配时间，提高工作效率。

在开源社区寻找所需要的工具和库的时候，发现有很多优秀的代码库，但是缺少一个小型容易上手的项目流程或者使用教程，导致使用者需要花额外的时间去学习区分它，所以本项目提供了一个简单的代码库范本，希望可以帮助到他人。当然作者水平有限，代码不完善部分还望理解。

<span id="nav-4"></span>

## 相关项目演示

![](http://47.108.208.140:8002/i/2022/02/14/p99ph2.png)

<span id="nav-5"></span>

## 功能特色

- 请求脚本与项目分离，项目复用率高
- 前后端分离，维持项目完整性
- 页面简洁，程序交互完善
- 内置目录导航功能，解决部分 Markdown 解析引擎不能正确解析导航的问题

<span id="nav-6"></span>

## 架构

```
|—— .gitee                          Gitee 配置文件
| |—— ISSUE_TEMPLATE.md             Gitee Issue 模板
| |—— PULL_REQUEST_TEMPLATE.md      Gitee PR 模板
|—— .github                         Github 配置文件
| |—— ISSUE_TEMPLATE                Github Issue 模板
| | |—— issue-template-bug.md       Github Issue Bug 模板
| | |—— issue-template-feature.md   Github Issue Feature 模板
| |—— workflows                     Github 工作流
| | |—— deploy-for-hugo.yml         Github 工作流 Hugo 示例
| | |—— deploy-for-nodejs.yml       Github 工作流 NodeJS 示例
| |—— pull-request-template.md      Github PR 模板
|—— website                         项目网站
|—— CHANGELOG.md                    发布日志
|—— LICENSE                         许可证
|—— README.md                       英语 README
|—— README.zh-Hans.md               其他语言 README
|—— README.tmpl.md                  README 模板

```

<span id="nav-7"></span>

