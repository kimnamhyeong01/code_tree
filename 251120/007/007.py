secret_code, meeting_point, time = input().split()
time = int(time)
class Secret:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code 
        self.meeting_point = meeting_point 
        self.time = time 

secret1 = Secret(secret_code, meeting_point, time)
print('secret code :', secret1.secret_code)
print('meeting point :', secret1.meeting_point)
print('time :', secret1.time)