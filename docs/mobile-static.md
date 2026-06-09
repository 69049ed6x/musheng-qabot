# 手机端静态版部署说明

这个版本不需要 Python 服务端，也不需要 SQLite 运行在手机上。

运行方式：

- 手机浏览器打开 `static/mobile.html`
- 页面加载 `static/kb.json` 作为本地知识库
- 检索、上下文、风险提示都在手机浏览器里完成
- LLM 请求由手机浏览器直接发到用户填写的 API URL

## 使用前配置

页面右上角点 `API 设置`，填写：

- API URL
- 模型名称
- API Key

这三个字段默认都是空的。保存后只存在当前手机浏览器本地，不会写入代码文件。

## 更新知识库

修改 Word、图片文字资料或人工知识后，重新导出静态知识库：

```powershell
python -m qabot.export_static
```

生成文件：

```text
static/kb.json
```

## GitHub Pages 部署

可以把整个项目上传到 GitHub，然后在 GitHub Pages 里选择发布根目录。

访问地址示例：

```text
https://你的用户名.github.io/仓库名/static/mobile.html
```

## 手机添加到桌面

手机浏览器打开 `mobile.html` 后：

- iPhone Safari：分享按钮 -> 添加到主屏幕
- Android Chrome：菜单 -> 添加到主屏幕

## 注意

如果模型 API 不允许浏览器跨域请求，页面会提示 API 请求失败。这不是手机网页的问题，而是 API 服务不允许网页直接调用。那种情况下需要增加一个 Cloudflare Worker / Vercel Function 代理。
