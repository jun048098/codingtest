# def parking_time(in_time, out_time):
#     in_hour, in_min = map(int, in_time.split(':'))
#     out_hour, out_min = map(int, out_time.split(':'))
#     hour = out_hour - in_hour
#     if in_min <= out_min:
#         min = out_min - in_min
#     else:
#         min = out_min+60 -in_min
#         min = -60 + min
#     return  hour * 60 + min
def parking_time(in_time, out_time):
    in_hour, in_min = map(int, in_time.split(':'))
    out_hour, out_min = map(int, out_time.split(':'))
    in_time = in_hour * 60 + in_min
    out_time = out_hour * 60 + out_min
    return  out_time - in_time
def solution(fees, records):
    new_records = [i.split() for i in records]
    records_dict = {}
    record_time = {}

    answer = []
    for r in new_records:
        car_num = int(r[1])
        if r[2] == "IN":
            records_dict[car_num] = r[0]
        else:
            total_time = parking_time(records_dict[car_num],r[0])
            print(total_time)
            if car_num not in record_time:
                record_time[car_num] = total_time
            else:
                record_time[car_num] += total_time
            records_dict.pop(car_num)
    for num, time in records_dict.items():
        total_time = parking_time(time, '23:59')
        if num not in record_time:
            record_time[num] = total_time
        else:
            record_time[num] += total_time
    basic_time, basic_fee, extra_time, extra_fee = fees
    print(record_time)
    for num, time in record_time.items():
        if time <= basic_time:
            answer.append((num, basic_fee))
        else:
            all_time = (time - basic_time)/ extra_time
            if all_time == int(all_time):
                all_time = int(all_time)
                total_fee =  basic_fee + all_time * extra_fee
                answer.append((num, total_fee))
            else:
                total_fee = basic_fee + int(all_time +1) * extra_fee
                answer.append((num, total_fee))

    answer.sort()
    return [i[1] for i in answer]

f=[180, 5000, 10, 600]
r = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(f, r))
'''
1. 리코드 split()
for문
    2. in이면 딕셔너리 추가
    3. out 이면 딕셔너리 계산 딕셔너리 pop 리스트에 추가
4. 남은 딕셔너리 23:59로 계산
5. 리스트sort

함수 시간 계산
'''


