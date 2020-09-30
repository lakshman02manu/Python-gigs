import winsound
#duration of the play
duration=1000
#frequencies to the musical notes of Sa Re Ga Ma Pa Da Ni Sa
freq=[261,294,330,349,392,440,494,515,515,494,440,392,349,330,294,261]
for i in freq:
    winsound.Beep(i,duration)
