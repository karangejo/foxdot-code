child = [2/5, 3/5, 5/5]
mother = [2/5, 2/5, 4/5, 2/5]
father = [2/5, 1/5, 2/5]
clapping_music = [1/8, 1/8, 1/4, 1/8, 1/4, 1/4, 1/8, 1/4]
rtlis=[father, mother, child]
bpm = 120
players= []
for i in range(3):
    players.append(Player())
    players[i] >> blip(oct=i+2, dur=rtlis[i], bpm=bpm)
    
print(SynthDefs)
    
Clock.clear()


