import random

# 20分ゲーム作成
# 一致桁数 0 ~ 3
# 一致場所 0 ~ 3
if __name__ == "__main__":
    num = random.randint(100, 999)
    while str(num)[0] == str(num)[1] or str(num)[0] == str(num)[2] \
            or str(num)[1] == str(num)[2]:
        num = random.randint(100, 999)
    while True:
        input_num = input("input >> ")
        unique_num = len(list(set(str(input_num)) & set(str(num))))
        unique_digit = 0
        for i in range(3):
            if str(input_num)[i] == str(num)[i]:
                unique_digit += 1
        if str(input_num) == str(num):
            print("べ、別に当たったわけじゃないんだからねっ...///")
            break
        print("一致桁数 : {0}\n一致場所 : {1}".format(unique_num, unique_digit))
