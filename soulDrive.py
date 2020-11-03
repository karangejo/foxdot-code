print(SynthDefs)

Clock.bpm = 90

Scale.default = Scale.dorian

var.prog = var([[0,4]],4)

p1 >> razz(var.prog, dur=4) + (0,2,4)

b1 >> jbass(var.prog, dur=PDur(7,12), formant=0, drive=0.1).every(4, "shuffle") + [0,2,4,6]

d1 >> play("xxtd[--]xoo [--]", amp=2).every(4, "reverse")

g1 >> sawbass(var.prog, oct=6, dur=1/4, drive=0.1) + (6,2,4)

a1 >> sitar(var.prog, oct=8, dur=PDur(8,12)).every(4, "stutter", 2).every(4, "reverse") + [[0,8,4,2,6]]

Clock.clear()
