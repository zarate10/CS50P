def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def with_numbers(s, n):
        for i in range(len(s)):
            for j in range(len(n)):
                if s[i] == n[j]:
                    return True

def is_valid(s):
    if len(s) >= 2 and len(s) <= 6 and s.isalnum():

        n = ['0','1','2','3','4','5','6','7','8','9']

        if with_numbers(s, n):
            middle = len(s) // 2
            last_number = []
            arr_last = []

            for i in range(2):
                for j in range(len(n)):
                    if n[j] == s[i]:
                        return False

            for i in range(middle, len(s)):
                arr_last.append(s[i])
                for j in range(len(n)):
                    if s[i] == n[j]:
                        last_number.append(s[i])

            if last_number != arr_last or last_number[0] == '0':
                return False
    
            return True
        return True
    return False


main()
