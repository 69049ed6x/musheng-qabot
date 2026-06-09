# 沐笙清谷本地客服问答机器人

这是一个本地可运行的知识库客服回复机器人。它会把 Word 文档、图片人工摘要、体验版食用方法和客服跟进话术写入 SQLite 数据库，然后提供电脑浏览器聊天页面和微信小程序可调用的 HTTP API。

## 当前能力

- 资料入库：`data/sources` 里的 `.docx` + 图片人工摘要 + 手工整理客服知识。
- 本地数据库：SQLite，重新入库命令为 `python -m qabot.ingest`。
- 回答方式：先检索对应专业知识，再生成“建议回复客户”，并附“参考依据”。
- LLM 润色：可选接入 DeepSeek，把规则草稿润色成更自然的客服话术；未配置或调用失败时自动使用规则版回答。
- 风险边界：涉及疾病、用药、孕哺、严重不适等问题时，返回 `needs_human: true`，提示医生或一对一导师确认。
- 本地页面：`http://127.0.0.1:8000`。
- 小程序接口：`POST /api/chat`。

## 启动

```powershell
$py = "C:\Users\24512\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py -m qabot.ingest
& $py -m qabot.server
```

然后打开：

```text
http://127.0.0.1:8000
```

## DeepSeek 配置

不配置 DeepSeek 时，系统会继续使用本地规则版回答。要开启 LLM 润色，在启动服务前设置环境变量：

```powershell
$env:DEEPSEEK_API_KEY = "你的 DeepSeek API Key"
$env:DEEPSEEK_BASE_URL = "https://api.deepseek.com"
$env:DEEPSEEK_MODEL = "deepseek-v4-pro"
```

LLM 只根据本地检索资料和规则草稿润色客服回复。涉及疾病、用药、孕哺、严重不适时，风险判断仍由本地规则保留，接口会继续返回 `needs_human: true`。

## 接口

```http
POST http://127.0.0.1:8000/api/chat
Content-Type: application/json

{
  "message": "体验版怎么喝？"
}
```

返回包含：

- `answer`：可直接参考的客服回复 + 资料依据。
- `sources`：命中的知识来源。
- `needs_human`：是否建议人工确认。
- `used_llm`：本次是否成功使用 DeepSeek 润色。

## 资料说明

用户提供的公众号链接 `https://mp.weixin.qq.com/s/D8cfiFZi4gCg3p7dNC1bOQ` 当前环境未能直接抓取正文。已先把用户粘贴的“辟谷餐体验版食用方法、注意事项、排便反应、每日变化、打卡话术”等内容作为权威资料入库。

## 测试

```powershell
$py = "C:\Users\24512\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $py -m unittest discover -s tests -v
```
