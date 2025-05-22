import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,28))
r=w0.sketch().arc((-16,-40),(16,-6),(-9,34)).arc((-100,5),(-16,-40)).assemble().push([(-48,0)]).circle(49,mode='s').finalize().extrude(-57).union(w0.sketch().push([(-7,15)]).circle(26).reset().face(w0.sketch().segment((88,41),(95,35)).segment((100,41)).segment((92,47)).close().assemble()).finalize().extrude(-57))