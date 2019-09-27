num = int(input('How many numbers: '))
total_sum = 0
tot_num = []
for n in range(0, num):
    numbers = float(input('Enter number : '))
    tot_num.append(numbers)
    total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)
count = 0
for n in tot_num:
    if(n < avg):
       count = count+1

print(count)
cod = 0
for n in tot_num:
    if(n == avg):
        cod = cod+1

print(cod)        
