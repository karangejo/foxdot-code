Clock.bpm = 90

print(SynthDefs)

p2 >> prophet([(1,3,5),(3,5,8)], dur=[2])

p3 >> bass([1], dur= [1/2,1/2,rest(1)])

p4 >> keys([1,3,5,8], dur=[1/2,rest(1/4),1/4])

p5 >> play("x-x-")

p6 >> play("[--]-c-[--]-o")

p7 >> pulse([3,5,8], oct=6, dur=[1/4,1/2, rest(1/4),rest(1)])

p8 >> sitar([(5,3),(1,8)],  oct=5, dur=[1/4], amp=2/3)

p9 >> pulse([(1,3,5,8)], dur=[rest(1),1], amp=1)

p8.stop()

Clock.clear()
