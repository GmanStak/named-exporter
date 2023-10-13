# named-exporter
解析域名，返回prometheus Metrics
# 程序说明及注意事项
本地需要配置你的dns地址，原理是本地访问你的dns地址配置的域名，判断是否可用
# 配置文件说明（config.json）
dns_ip": "你的dns服务器地址，不在域名判断逻辑中，也可以随便写",
"hostname": "你的dns服务器主机名，随便写也可以",
"domain": "你的dns服务器配置的域名，同一个服务器不同域名需要添加多条，后续有时间会优化成一个列表"
# 程序启动参数说明
"-a","--ipaddress" 监听地址，默认：localhost，启动建议：0.0.0.0
"-p","--port" 监听端口，默认：9098
"-c","--config" 配置文件路径，默认："./conf/config.json"


