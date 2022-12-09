#!/usr/bin/python3
import random


# Amir Capital crypto protsentini hisoblash



# # invest = 0.05782
# invest = 0.356
data = 52
# foiz = 0.05
list_foiz = [7,29,5.8,10,9.8,3.8,6.4,8.4,8.1,9.5,9,4.2,6,10,8.5,4.4,15.4,15.4,5.2,13.7,11.7,21,12.7,5,5.2,4.7,6.1,8.7,5.7,3.1,5.7,4,3,3.4,6.7,7.2,10.5,10.2,8.8,9.1,13.5,6.7]

sum_foiz = 0
for i in range(len(list_foiz)):
  sum_foiz += i

mean_foiz = sum_foiz / len(list_foiz) / 10
foiz = mean_foiz
print(foiz)


def main():
  print("Investitsiya Crypto qiymatini hisoblash!")
  invest = float(input("Crypto qiymati kiriting (Exemple: 0.12)\n"))
  # data = input("investitsiya vaqtini kiriting Exemple: 12 (oy)\n")
  # foiz = float(input("investitsiya foyizini kiriting (Exemple: 5 (%))\n")) / 100

  return invest



def hisoblash(invest):
  base = invest
  j = 0
  t = 0
  k = 0
  l = 0
  n = 0

  for i in range(data):
    # foiz = random.randint(3, 7)
    # if foiz == 7:
    #   j += 1
    # if foiz == 6:
    #   t += 1
    # if foiz == 5:
    #   k += 1
    # if foiz == 4:
    #   l += 1
    # if foiz == 3:
    #   n += 1

    p = base * foiz / 100
    hisob1 = base + base * foiz / 100

    print(f"{i}   -- {foiz}%  --   {round(base, 4)} + {round(p, 4)} =  {round(hisob1, 4)}")
    base = hisob1

  # print(f"{data}   --  7% = {j}")
  # print(f"{data}   --  6% = {t}")
  # print(f"{data}   --  5% = {k}")
  # print(f"{data}   --  4% = {l}")
  # print(f"{data}   --  3% = {n}")
  print(f"{data}   --  {round(invest, 4)} = {round(base, 4)}")



if __name__ == "__main__":
  hisoblash(main())


# 20/07/19   0.41826214

# 56 + 13    >> 0.007886589

# 07/12/20    0.96243675


# 0.05653986   + x             0.00001606

# 0.05849206                   0.00004630

# 0.00822 %