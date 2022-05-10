# 미완
def solution(rooms, target):
    answer = []
    name_rooms = dict()
    room_name = dict()
    for info in rooms:
        room_num, workers = info[1:].split(']')
        room_num = int(room_num)
        workers = workers.split(',')
        if workers[0] == 'None':
            continue
        for worker in workers:
            if worker in name_rooms:
                name_rooms[worker].append(room_num)
            else:
                name_rooms[worker] = [room_num]
            if room_num in room_name:
                room_name[room_num].append(worker)
            else:
                room_name[room_num] = [worker]
    # name_rooms:           {'James': [403], 'Azad': [404, 101], 'Louis': [404], 'Andy': [404], 'Guard': [101]}
    # print(room_name):     {403: ['James'], 404: ['Azad', 'Louis', 'Andy'], 101: ['Azad', 'Guard']}

    # print(name_rooms)   {'Azad': [101], 'Guard': [101, 202, 303], 'Dzaz': [303]}
    # print(room_name)    {101: ['Azad', 'Guard'], 202: ['Guard'], 303: ['Guard', 'Dzaz']}

    if target in room_name:
        for rworker in room_name[target]:
            del name_rooms[rworker]
        del room_name[target]
    sname_rooms = sorted(name_rooms.items(), key = lambda item: len(item[1]))
    # print(sname_rooms) ==> [('Andy', [404]), ('Guard', [101]), ('Azad', [404, 101]), ('Louis', [404, 101])]
    # print(sname_rooms) ==> [('Azad', [101]), ('Dzaz', [303]), ('Guard', [101, 202, 303])]


    name_room_cnt = dict()
    for name, room in sname_rooms:
        name_room_cnt[name] = len(room)
    # print(name_room_cnt) ==> {'Louis': 1, 'Andy': 1, 'Guard': 1, 'Azad': 2}
    # print(name_room_cnt) ==> {'Andy': 1, 'Guard': 1, 'Azad': 2, 'Louis': 2}
    tmp_cnt = 0
    tmp_names = []
    for name, cnt in name_room_cnt.items():
        print(name, cnt)
        if tmp_names == None and tmp_cnt == 0:
            tmp_names.append(name)
            tmp_cnt = cnt
        else:
            if cnt == tmp_cnt:
                tmp_names.append(name)
            else:
                # 1. 각자의 방 중에서 타겟과 가장 가까운 방 구하기
                name_nearest_room_gap = []
                for tmp_name in tmp_names:
                    min_gap = 9999
                    min_room = 10000
                    for room in name_rooms[tmp_name]:
                        if abs(target - room) < min_gap:
                            min_gap = abs(target - room)
                            min_room = room
                    name_nearest_room_gap.append((tmp_name, min_room, min_gap))
                # print(name_nearest_room_gap)

                # 2. 누구의 방이 더 타겟에 가까운지
                sname_nearest_room_gap = sorted(name_nearest_room_gap, key=lambda x: (x[2], x[0]))
                # print(sname_nearest_room_gap)
                for info in sname_nearest_room_gap:
                    answer.append(info[0])
                # print(name_nearest_room_gap)

                # 다 끝나면
                tmp_names.clear()
                tmp_names.append(name)
                tmp_cnt = cnt
                print(tmp_names, tmp_cnt)

    print(tmp_names)
    if tmp_names:
        # 1. 각자의 방 중에서 타겟과 가장 가까운 방 구하기
        name_nearest_room_gap = []
        for name in tmp_names:
            min_gap = 9999
            min_room = 10000
            for room in name_rooms[name]:
                if abs(target - room) < min_gap:
                    min_gap = abs(target - room)
                    min_room = room
            name_nearest_room_gap.append((name, min_room, min_gap))
        # print(name_nearest_room_gap)

        # 2. 누구의 방이 더 타겟에 가까운지
        sname_nearest_room_gap = sorted(name_nearest_room_gap, key=lambda x: (x[2], x[0]))
        # print(sname_nearest_room_gap)
        for info in sname_nearest_room_gap:
            answer.append(info[0])

    return answer

print(solution(["[1234]None,Of,People,Here","[5678]Wow"], 1234))

# 해당 방에 이미 지정 자리가 있는 직원은 제외합니다. --> 우선순위에 미포함
# 지정 자리가 제일 적은 직원의 우선순위가 가장 높습니다. --> 모든 직원의 지정 자리 개수 계산 필요
    # 지정 자리의 개수가 동일한 사람들끼리는 새 자리가 생긴 방에서 가장 가까운 방에 지정 자리가 있는 직원이 우선순위가 더 높습니다.
    # 한 사람의 지정 자리가 여러 개인 경우, 지정 자리가 있는 방 중에서 새 자리가 생긴 방과 가장 가까운 방을 기준으로 선정합니다.
    # 지정 자리 수와 새 자리가 생긴 방까지의 거리도 동일한 경우, 이름이 사전 순으로 빠른 사람이 더 높은 우선순위를 갖습니다.
        # 단 사전 순은 대문자가 소문자 보다 사전 순으로 앞섭니다. 예를 들어, A~Z, a~z까지 알파벳을 사전 순으로 정렬한 결과는 [A, B, ... Z, a, b, ... , z]입니다