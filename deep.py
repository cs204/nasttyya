answer=input("Какой ответ на главный вопрос жизни, вселенной и всего такого?")
match answer.lower():
    case"42":
        print(" Да")
    case"сорок два":
        print(" Да")
    case _:
        print(" No")
