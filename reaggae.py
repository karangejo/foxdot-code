print(SynthDefs)

var.prog = var([0,3,0,4],4)

p1 >> bug(var.prog, oct=6, dur=[1,1/4,1/4,1/2]) + (0,2,4)

b1 >> bass(var.prog, dur=[1/2,rest(1),1/2])

d1 >> play("-xx-[--]-x").every(4, "reverse")

sn >> play("--{o-}-").every(2, "reverse")

s1 >> sitar(var.prog + [0,2,4,6], dur=PDur(14,24)).every(2, "stutter", 2).every(4, "reverse")

r1 >> pasha(var.prog, oct=7) + [[0,2,4]]

r1.solo(0)

s1.stop() 

Clock.clear()
