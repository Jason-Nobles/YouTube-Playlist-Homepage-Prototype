# Author: Jason Nobles
# COMP163, Section 003
#
#
# CONSTANTS set below
moving_truck_capacity = 1600
warehouse_location = 0

# variables set below
pickup_location = float(input('Where is the next pickup? '))
pickup_size = float(input('How large is the next pickup? '))

drop_off = 0
drop_off_size = 0
total_storage = 0


# rest of code below 
while drop_off < 3: 
    drop_off_adder = 0
    at_warehouse = 0
    while at_warehouse == 0:
        if pickup_location == 0 or pickup_location <= 5 and pickup_location >= -5 and pickup_size > 0 and pickup_size <= moving_truck_capacity:
            drop_off_size += pickup_size
            print('Pickup at: {}, Size {} cubic feet'.format(pickup_location, pickup_size))
            at_warehouse = 1
        else:
            print('Declined.')
            pickup_location = float(input('Where is the next pickup? '))
            pickup_size = float(input('How large is the next pickup? '))
    while at_warehouse == 1:
        warehouse_location = pickup_location
        pickup_location = float(input('Where is the next pickup? '))
        pickup_size = float(input('How large is the next pickup? '))
        if pickup_location >= 0 and pickup_location < warehouse_location:
            if drop_off_size + pickup_size <= moving_truck_capacity and pickup_size > 0 and pickup_size <= moving_truck_capacity and pickup_location <= 10 and pickup_location >= -10:
                drop_off_size += pickup_size
                print('Pickup at: {}, Size {} cubic feet'.format(pickup_location, pickup_size))
            else:
                drop_off += 1
                drop_off_adder += drop_off_size 
                total_storage += drop_off_adder
                print('Declined')
                print('Drop-off Size: {} cubic feet'.format(drop_off_adder))
                drop_off_size = 0
                if drop_off == 3:
                    print('All Done. Total storage amount: {} cubic feet'.format(total_storage))
                    break
                else:
                    at_warehouse = 0
                    pickup_location = float(input('Where is the next pickup? '))
                    pickup_size = float(input('How large is the next pickup? '))
        elif pickup_location <= 0 and pickup_location > warehouse_location:
            if drop_off_size + pickup_size <= moving_truck_capacity and pickup_size > 0 and pickup_size <= moving_truck_capacity and pickup_location <= 10 and pickup_location >= -10:
                drop_off_size += pickup_size
                print('Pickup at: {}, Size {} cubic feet'.format(pickup_location, pickup_size))
            else:
                drop_off += 1
                drop_off_adder += drop_off_size 
                total_storage += drop_off_adder
                print('Declined')
                print('Drop-off Size: {} cubic feet'.format(drop_off_adder))
                drop_off_size = 0
                if drop_off == 3:
                    print('All Done. Total storage amount: {} cubic feet'.format(total_storage))
                    break
                else:
                    at_warehouse = 0
                    pickup_location = float(input('Where is the next pickup? '))
                    pickup_size = float(input('How large is the next pickup? '))
        elif pickup_location == pickup_location <= warehouse_location + 2 and pickup_location >= warehouse_location - 2:
            if drop_off_size + pickup_size <= moving_truck_capacity and pickup_size > 0 and pickup_size <= moving_truck_capacity and pickup_location <= 10 and pickup_location >= -10:
                drop_off_size += pickup_size
                print('Pickup at: {}, Size {} cubic feet'.format(pickup_location, pickup_size))
            else:
                drop_off += 1
                drop_off_adder += drop_off_size
                total_storage += drop_off_adder
                print('Declined')
                print('Drop-off Size: {} cubic feet'.format(drop_off_adder))
                drop_off_size = 0
                if drop_off == 3:
                    print('All Done. Total storage amount: {} cubic feet'.format(total_storage))
                    break
                else:
                    at_warehouse = 0
                    pickup_location = float(input('Where is the next pickup? '))
                    pickup_size = float(input('How large is the next pickup? '))
        else:
            drop_off += 1
            drop_off_adder += drop_off_size
            total_storage += drop_off_adder
            print('Declined')
            print('Drop-off Size: {} cubic feet'.format(drop_off_adder))
            drop_off_size = 0
            if drop_off == 3:
                print('All Done. Total storage amount: {} cubic feet'.format(total_storage))
                break
            else:
                at_warehouse = 0
                pickup_location = float(input('Where is the next pickup? '))
                pickup_size = float(input('How large is the next pickup? '))