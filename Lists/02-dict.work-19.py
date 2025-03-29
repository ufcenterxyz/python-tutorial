
student_info=[{
    "name":"li",
    "age":30,
    "course":{
        "English":90,
        "Math":100
    }
},
{
    "name":"m",
    "age":30,
    "course":{
        "English":80,
        "Math":76
    }
},
]
name_info=student_info[0]["name"]
score_info=student_info[0]["course"]["English"]

print(f"name: {name_info} , score: {score_info}")