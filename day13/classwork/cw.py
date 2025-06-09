heart_rate = int(input('enter your heart_rate: '))

if heart_rate > 180:
    print('your heart rate is high')
elif 160 <= heart_rate <= 170:
    print('heart rate is normal')
else:
    print('your heart rate is low')