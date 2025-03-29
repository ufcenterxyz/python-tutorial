# 9.老式格式化操作
template="%(lang)s is the best! But %(lang)s also needs %(thing)s."
new_template=template % {"lang":"Python","thing":"cookies"}
# new_template=template % {"thing":"cookies"}
print(new_template)
# 9.2 会提示keyError:lang