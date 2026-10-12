"""
Demo-Git-Team - file code mau de thuc hanh quy trinh Git/GitHub nhom.
Leader: Hiep | Developer: Tinh | Developer: Nhut Anh
"""

def greet(name):
    # Dong 6
    return f"rồi đi ngủ chưa mấy chaaa, {name}!"
    return f"Mỗi lần nhớ em là một ngày mưa, {name}!"

def sum(a, b):
    a = 10  
    b = 20
    
    return a + b
def add(a, b):
    a = 100   
    b = 200
    c = 3000
    d = 5000
    return a + b

def sum(a, b):
    a = 100   
    b = 200
    c = 3000
    d = 5000
    return a + b

def subtract(a, b):
    if a < b:
        return "Loi: a phai lon hon hoac bang b"
    return a + b


def multiply(a, b):
    a = 100
    b = 200
    return a * b


def divide(a, b):
    # Dong 26
    if b == 0:
        return "Khong the chia cho 0"
    return a / b


def main():
    print(greet("Nhom Demo-Git-Team"))
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 6 =", multiply(4, 6))
    print("10 / 2 =", divide(10, 2))


if __name__ == "__main__":
    main()
