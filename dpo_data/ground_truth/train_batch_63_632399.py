import cadquery as cq
w0=cq.Workplane('YZ',origin=(-23,0,0))
r=w0.sketch().push([(-16,-73)]).circle(27).reset().face(w0.sketch().arc((-6,66),(-2,61),(2,55)).arc((37,91),(-6,66)).assemble()).push([(12,74)]).circle(11,mode='s').finalize().extrude(46)