import calendar
days = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
mm, dd, yr = list(map(int, input().split()))

print(days[calendar.weekday(yr, mm, dd)])

