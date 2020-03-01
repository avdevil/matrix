# Python Program - Make Simple Calculator
import requests

def banner():
    print(r"                       __  __ ___ _  _ ___                        ")
    print(r"                      |  \/  |_ _| \| |_ _|                       ")
    print(r"                      | |\/| || || .\`|| |                        ")
    print(r"                      |_|  |_|___|_|\_|___|                       ")
    print(r"   _____ __  __  _____   ____   ____  __  __ ____  ______ _____   ")
    print(r"  / ____|  \/  |/ ____| |  _ \ / __ \|  \/  |  _ \|  ____|  __ \  ")
    print(r" | (___ | \  / | (___   | |_) | |  | | \  / | |_) | |__  | |__) | ")
    print(r"  \___ \| |\/| |\___ \  |  _ <| |  | | |\/| |  _ <|  __| |  _  /  ")
    print(r"  ____) | |  | |____) | | |_) | |__| | |  | | |_) | |____| | \ \  ")
    print(r" |_____/|_|  |_|_____/  |____/ \____/|_|  |_|____/|______|_|  \_\ ")
    print(r"                                                                  ")
print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");
print("5. Exit");
choice = int(input("Enter your choice: "));
if (choice>=1 and choice<=4):
    print("Enter two numbers: ");
    num1 = int(input());
    num2 = int(input());
    if choice == 1:
    	res = num1 + num2;
    	print("Result = ", res);
    elif choice == 2:
    	res = num1 - num2;
    	print("Result = ", res);
    elif choice == 3:
    	res = num1 * num2;
    	print("Result = ", res);
    else:
    	res = num1 / num2;
    	print("Result = ", res);
elif choice == 5:
    exit();
else:
    print("Wrong input..!!");
banner()
