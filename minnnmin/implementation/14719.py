height, width = map(int, input().split())
blocks = list(map(int, input().split()))

n = 1  # block cnt
left = blocks[0]
between_blocks = []
rain_sum = 0
for b in blocks[1:]:
    if n == width - 1:
        right = b
        if right >= left:
            if between_blocks:
                std = left if left < right else right
                for bb in between_blocks:
                    rain_sum += std - bb
        else: # problem
            tmp_between_blocks = []
            between_blocks.reverse()
            for bb in between_blocks:
                if tmp_between_blocks:
                    if bb >= right:
                        tmp_left = bb
                        std = tmp_left if tmp_left < right else right
                        for tbb in tmp_between_blocks:
                            rain_sum += std - tbb
                        tmp_between_blocks.clear()
                        right = bb
                    else:
                        tmp_between_blocks.append(bb)
                else: # tmp_between_blocks is empty
                    if bb >= right:
                        right = bb
                    else:
                        tmp_between_blocks.append(bb)
            if tmp_between_blocks:
                std = left if left < right else right
                for tbb in tmp_between_blocks:
                    rain_sum += std - tbb
    else:
        if b < left:
            between_blocks.append(b)
            n += 1
        else:
            if not between_blocks: # between_blocks is empty
                left = b
                n += 1
            else:
                right = b
                if between_blocks:
                    std = left if left < right else right
                    for bb in between_blocks:
                        rain_sum += std - bb
                    between_blocks.clear()
                    left = right
                    n += 1
print(rain_sum)