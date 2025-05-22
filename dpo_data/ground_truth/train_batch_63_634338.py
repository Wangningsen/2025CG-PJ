import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
r=w0.sketch().arc((-98,13),(-24,-12),(-9,-89)).segment((100,-89)).segment((100,59)).segment((48,59)).arc((31,72),(10,67)).arc((2,75),(-8,81)).segment((-8,85)).segment((-16,85)).arc((-38,89),(-60,85)).segment((-68,85)).segment((-68,81)).arc((-95,52),(-98,13)).assemble().finalize().extrude(-61)