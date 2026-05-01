# Vuln Analysis Agent

一个运行在 Kali 上的 AI 安全分析代理，自动读取 Nmap 扫描结果，调用大语言模型生成漏洞风险报告，并输出修复建议。

## 解决的痛点
手工审阅上百行 Nmap 输出既慢又容易遗漏高危漏洞组合。本 Agent 利用长链推理将零散端口信息串联成攻击链分析，大幅提升效率。

## 核心流程
1. 通过 Nmap 对目标进行服务版本扫描
2. 将输出传递给 OpenAI 兼容 API（DeepSeek / 智谱等）
3. AI 模型按“高危预警 + 可利用风险组合 + 修复建议”的结构化格式输出报告
4. 保存分析结果到本地文件

## 运行方法
- 环境要求：Python 3, pip install openai
- 注册 DeepSeek（或其他 API），获取 Key
- 修改脚本中的 `api_key` 和 `base_url`
- 执行扫描：`sudo nmap -sV -T4 scanme.nmap.org > /root/scan_result.txt`
- 运行分析：`sudo /home/kali/ai_env/bin/python3 /home/kali/vuln_agent.py`

## 作者
小白安全爱好者，使用 Kali 虚拟机开发。
