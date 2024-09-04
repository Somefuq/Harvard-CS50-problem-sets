def main():
    x= input('provide......').lower().strip()
    time= convert(x)

    if 7.00 <= time <= 8.00:
        print('Breakfast time')
    elif 12.00 <= time <= 13.00:
        print('Lunch time')
    elif 18.00<=time<=19.00:
        print('dinner time')
    else:
        None

def convert(time):
    h= time.split(':')[0]
    m= time.split(':')[1]
    if 'a.m.' or 'p.m.' in m:
        m= m.split(' ')[0]
    else:
        m= m

    xh= int(h)
    xm= int(m)/60

    if xh<24:
        if 'a.m.' in time:
            if xh==12:
                xh=xm
            else:
                xh=xh+xm
        elif 'p.m.' in time:
            if xh!= 12:
                xh= 12+xh+xm
            else:
                xh=xh+xm
        else:
            xh=xh+xm
    elif xh==24:
        xh=xm
    else:
        return None
    return xh
# Random comment
if __name__ == "__main__":
    main()



