# Проверяет монотонность в порядке возрастания
def is_monotonic(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True


while True:
    print("Вход (введите значения списка через пробел): ")
    nums = [int(i) for i in input('nums = ').split()]
    #Если введенный список монотонный или введенный перевернутый список монотонный, то True 
    if is_monotonic(nums) or is_monotonic(list(reversed(nums))):
        print("Вывод: True")
    else:
        print("Вывод: False")
