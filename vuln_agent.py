#!/usr/bin/env python3
import sys
from openai import OpenAI

# ===== 修改这里 =====
# 1. 如果你用 DeepSeek，保留下面两行；如果用 OpenAI 官方，需改 base_url
client = OpenAI(
    api_key="sk-ca1c7c2b854c4c6fbeecb2f327fa4fe4",   # 填你的真实 Key
    base_url="https://api.deepseek.com"  # DeepSeek 的地址
)
MODEL = "deepseek-chat"   # 便宜，够用

# 2. 读取上一步生成的扫描报告
try:
    with open("/root/scan_result.txt", "r") as f:
        scan_content = f.read()
except FileNotFoundError:
    print("错误：请先运行 nmap 扫描生成 scan_result.txt")
    sys.exit(1)

# 3. 构建给 AI 的指令（即你的 Agent 核心提示词）
prompt = f"""你是一名资深安全分析师。下面是一份 Nmap 服务扫描结果。
请你严格按以下结构输出内容，不要添加无关信息：

1. 【高危漏洞预警】列出可能被远程利用的高危服务及版本（如 OpenSSH 旧版本、数据库弱口令风险等）。
2. 【可被利用的风险组合】如果多个开放端口组合可能造成攻击链，请指出来。
3. 【修复建议】用简洁的语言给出每一条的具体修复步骤。

扫描结果：
{scan_content}
"""

# 4. 调用 AI
print("Agent 正在分析扫描报告...")
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "你是一个严密且只输出纯文本的安全分析 Agent。"},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
    max_tokens=1000
)

# 5. 输出最终报告
report = response.choices[0].message.content
print("\n" + "="*50)
print("       自动化安全分析报告       ")
print("="*50)
print(report)

# 6. 同时保存为文件，方便截图
with open("/root/ai_report.txt", "w") as f:
    f.write(report)
print("\n报告已保存至 /root/ai_report.txt")
