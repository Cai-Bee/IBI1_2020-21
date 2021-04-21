#define function of grade calculating
def calculator():
    name = input('Student name?')
    portfolio = input('Student grade for the code portfolio?')
    poster = input('Student grade for the poster presentation')
    exam = input('Student grade in the final exam?')
    final_score = 0.4*float(portfolio) + 0.3*float(poster) + 0.3*float(exam)
    return name+"    final grade: "+str(final_score)


#example of how the function should be called
calculator()
Someone
95
87
92
