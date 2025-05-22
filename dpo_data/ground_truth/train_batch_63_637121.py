import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,33))
r=w0.sketch().push([(-42,13)]).rect(70,18).push([(22,-58)]).circle(42).reset().face(w0.sketch().arc((13,23),(34,54),(30,17)).arc((49,98),(13,23)).assemble()).finalize().extrude(-66)