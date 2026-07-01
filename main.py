username = input("Enter Username: ")
password = input("Enter Password: ")
if username != "admin" or password != "1234":
    print("Login Failed")
    exit()
print("\nLogin Successful! Welcome Admin")
vehicles = []
while True:
    print("\n=================================")
    print("     TOLL TAX MANAGEMENT SYSTEM")
    print("=================================")
    print("1. Add Vehicle Entry")
    print("2. View All Vehicles")
    print("3. Search Vehicle")
    print("4. Daily Report")
    print("5. Total Tax Collection")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        vehicle_no = input("Enter Vehicle Number: ")
        vehicle_type = input("Enter Vehicle Type (Car/Bike/Truck): ")
        owner = input("Enter Owner Name: ")
        vtype = vehicle_type.lower()
        if vtype == "bike":
            tax = 20
        elif vtype == "car":
            tax = 50
        elif vtype == "truck":
            tax = 100
        else:
            tax = 30
        vehicle = {
            "number": vehicle_no,
            "type": vehicle_type,
            "owner": owner,
            "tax": tax
        }
        vehicles.append(vehicle)
        print("\nVehicle Added Successfully!")
        print("Toll Tax:", tax)
    elif choice == "2":
        if len(vehicles) == 0:
            print("\nNo Vehicles Found.")
        else:
            print("\n========== VEHICLE LIST ==========")
            for v in vehicles:
                print("---------------------------------")
                print("Vehicle Number :", v["number"])
                print("Vehicle Type   :", v["type"])
                print("Owner Name     :", v["owner"])
                print("Toll Tax       :", v["tax"])
    elif choice == "3":
        search_no = input("Enter Vehicle Number: ")
        found = False
        for v in vehicles:
            if v["number"] == search_no:
                print("\nVehicle Found")
                print("---------------------------------")
                print("Vehicle Number :", v["number"])
                print("Vehicle Type   :", v["type"])
                print("Owner Name     :", v["owner"])
                print("Toll Tax       :", v["tax"])
                found = True
                break
        if not found:
            print("\nVehicle Not Found")
    elif choice == "4":
        if len(vehicles) == 0:
            print("\nNo Vehicles Today.")
        else:
            total_tax = 0
            car = bike = truck = 0
            print("\n========== DAILY REPORT ==========")
            for v in vehicles:
                print("---------------------------------")
                print("Vehicle Number :", v["number"])
                print("Vehicle Type   :", v["type"])
                print("Toll Tax       :", v["tax"])
                total_tax += v["tax"]
                if v["type"].lower() == "car":
                    car += 1
                elif v["type"].lower() == "bike":
                    bike += 1
                elif v["type"].lower() == "truck":
                    truck += 1
            print("\nSUMMARY")
            print("Cars  :", car)
            print("Bikes :", bike)
            print("Trucks:", truck)
            print("\nTotal Tax Collection:", total_tax)
    elif choice == "5":
        total = 0
        for v in vehicles:
            total += v["tax"]
        print("\nTotal Toll Collection:", total)
    elif choice == "6":
        print("\nThank you Admin")
        break
    else:
        print("\nInvalid Choice")