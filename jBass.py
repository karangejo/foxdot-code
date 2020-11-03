print(SynthDefs)

Scale.default = Scale.minor

Clock.bpm = 100

p1 >> sinepad([0,3], dur=4) + (0,2,4) 

p2 >> jbass(var([0,3,5],PDur(13,16)), dur=[1/2, 1/2, rest(2)])

p3 >> play("[--](-o)x")

p4 >> play("X--[-(-x-)]")

p5 >> nylon([0], dur=1).every(8, "stutter", 2).every(4, "reverse") 

k1 >> pasha([0,0,3,5,7], dur=PDur(5,12)).every(4, "reverse")

l1 >> donk([5],dur=[1/4,1/4,rest(1)], oct=7).every(4, "reverse")

t1 >> sitar([0], dur=PDur(7,20)).every(16, "stutter", 2)

Clock.clear()
