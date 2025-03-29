score={
    "stu_1":100,
    "stu_2":120,
    "stu_3":100,
    "stu_4":100,
    "stu_5":100
}

score_info=score.values()
new_score=list(score_info)
print(new_score)

score_final={
    "max":max(new_score),
    "min":min(new_score),
    "sum":sum(new_score),
    "avarge":sum(new_score)/len(new_score)
}
print(score_final)
max_info=max(new_score)
print(max_info)
#找出获得最高分的学生
for i in score:
    if score[i]==max_info:
        print(i,score[i])
