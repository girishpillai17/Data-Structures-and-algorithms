def tof(num_disk, from_pole, aux_pole, to_pole):
    if num_disk == 1:
        print('move disk', num_disk, 'from', from_pole, 'to', to_pole) 

    else:
        tof(num_disk-1, from_pole, to_pole, aux_pole)
        print('move disk',num_disk,'from', from_pole, 'to', to_pole)
        tof(num_disk-1, aux_pole, from_pole, to_pole)

tof(3,1,2,3)