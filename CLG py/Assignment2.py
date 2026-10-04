queue = []

while True:
    print("\n1.Enqueue 2.Dequeue 3.Display 4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        queue.append(input("Customer: "))
    elif ch == 2:
        print("Served:", queue.pop(0) if queue else "Empty")
    elif ch == 3:
        print("Queue:", queue)
    elif ch == 4:
        break