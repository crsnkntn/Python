# Question 2B from the Google Foobar challenge

# The problem is: 
#        '>' = Person walking right
#        '<' = Person walking left
#        '-' = Space
#        
#        When a person walking right crosses a person walking left they must salute eachother
#
#        Count the number of salutes that occur if each person walks in their direction and return this number
#
#        For example, '<<>><' will return 4

def solution(s: str) -> int:
    i, j = 0, len(s) - 1
    while i <= j and s[i] != '>':
        i += 1
    found = True
    salutes = 0
    while found and i < j:
        iter = i + 1
        found = False
        while iter <= j:
            if (not found) and s[iter] == '>':
                found = True
                i = iter
            if s[iter] == '<':
                salutes += 2
            iter += 1
    return salutes



if __name__ == "__main__":
    s = "--->-><-><-->-"
    s2 = ">>>>>>>>>>>--------><"
    s3 = "<----<---<"
    s4 = ">---->>>----<"
    s5 = "<<>><"
    print(solution(s))
    print(solution(s2))
    print(solution(s3))
    print(solution(s4))
    print(solution(s5))