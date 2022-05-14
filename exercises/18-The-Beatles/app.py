# Your code here!!
def sing():
    song=""
    for i in range(10):
        if(i==4):
            song += "whisper words of wisdom, "
        if(i==9):
            song += "there will be an answer, "
        if(i == 9):
            song += "let it be"
        else:  
            song+="let it be, "
    return song
print(sing())