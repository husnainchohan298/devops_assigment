import time


def calc_square(numbers):
    result=[]
    for n in numbers:
        time.sleep(0.5)
        result.append(n*n)
    return result

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    start= time.time()
    squares=calc_square(numbers)
    end=time.time()
    print(f"Square : {squares}")
    print(f"Time taken : {end - start :.2f} seconds")