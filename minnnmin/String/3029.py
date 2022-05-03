nhh, nmm, nss = map(int, input().split(':'))
hh, mm, ss = map(int, input().split(':'))

if nhh > hh or (nhh == hh and nmm > mm) or (nhh == hh and nmm == mm and nss > ss):
    hh += 24

if nss > ss:
    if mm != 0:
        mm -= 1
        ss += 60
    else:  # mm == 0
        hh -= 1
        mm += 59
        ss += 60
if nmm > mm:
    hh -= 1
    mm += 60

rhh = str(hh - nhh)
rmm = str(mm - nmm)
rss = str(ss - nss)
if rhh == '0' and rmm == '0' and rss == '0':
    rhh = '24'

if int(rhh) < 10:
    rhh = '0' + rhh
if int(rmm) < 10:
    rmm = '0'+ rmm
if int(rss) < 10:
    rss = '0'+ rss

print(rhh + ':' + rmm + ':' + rss)