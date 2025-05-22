import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,5))
r=w0.sketch().push([(-35,-56)]).circle(44).reset().face(w0.sketch().segment((-11,25),(79,25)).segment((79,76)).segment((49,76)).arc((23,100),(-3,76)).segment((-11,76)).close().assemble()).push([(-8,68)]).circle(1,mode='s').finalize().extrude(-10)