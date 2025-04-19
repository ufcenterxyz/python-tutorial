lyrics="""
Here comes the sun
Here comes the sun
And I say
It's all right
"""
Chars=f"Total Chars: {len(lyrics)}"
print(Chars)

Lines=f"Total Lines: {len(lyrics.split("\n"))}"
print(Lines)

words=lyrics.upper()
final_words={}
out_put=""
for i in words:
    if final_words.get(i) is None:
        final_words[i]=1
        out_put+=i
print(out_put)
