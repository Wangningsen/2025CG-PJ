import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().segment((-83,-47),(11,-47)).arc((96,-26),(47,50)).segment((47,60)).segment((-83,60)).close().assemble().push([(-36,41)]).circle(13,mode='s').finalize().extrude(-29).union(w0.sketch().arc((-100,-45),(-80,-18),(-83,17)).segment((-100,17)).close().assemble().finalize().extrude(33))