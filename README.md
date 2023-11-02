## 说明
将clash大陆的ip地址规则集按照ipv4和ipv6分开为两个规则集。
数据来源：[Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules)

## 使用
可以在clash配置文件中的rule-providers中加入如下配置，其他配置可以根据需求自行配置
``` yaml
rule-providers:
  cncidr-v4:
    type: http
    behavior: ipcidr
    url: "https://raw.githubusercontent.com/CalebChen768/cn_ipv4_ipv6/main/ipv4.txt"
    path: ./ruleset/cncidr-v4.yaml
    interval: 86400
  cncidr-v6:
    type: http
    behavior: ipcidr
    url: "https://raw.githubusercontent.com/CalebChen768/cn_ipv4_ipv6/main/ipv6.txt"
    path: ./ruleset/cncidr-v6.yaml
    interval: 86400
```
