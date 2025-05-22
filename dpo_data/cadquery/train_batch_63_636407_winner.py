import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
w1=cq.Workplane('XY',origin=(0,0,-82))
r=w0.sketch().arc((-36,10),(-16,-89),(61,-37)).arc((60,85),(-36,10)).assemble().finalize().extrude(66).union(w1.sketch().push([(-35,-34)]).circle(65).push([(-23,-90)]).circle(7,mode='s').finalize().extrude(150))