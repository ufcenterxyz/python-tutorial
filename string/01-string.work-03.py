# 3.字符串拼接与性能
part1="Python "
part2="Rock!"

print(part1+part2)


print(part)

part_owe="%(part1)s" %{"part1":"Python "}
part_two="%(part2)s" %{"part2":"Rock!"}
print(part_owe +part_two)


part="%(part1)s %(part2)s" % {"part1":"Python ","part2":"Rock!"}
print('%s %s' % (part1, part2))
print(f'{part1} {part2}')

# 处理大量连接处理时，使用format或者%