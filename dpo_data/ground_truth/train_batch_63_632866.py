import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-83,2),(-28,-17)).arc((-11,-31),(11,-31)).segment((66,-50)).segment((83,-2)).segment((28,17)).arc((11,31),(-11,31)).segment((-66,50)).close().assemble().finalize().extrude(200)