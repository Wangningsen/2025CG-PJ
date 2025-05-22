import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
w1=cq.Workplane('XY',origin=(0,0,83))
r=w0.sketch().segment((-83,-19),(6,-19)).segment((6,26)).arc((32,17),(41,43)).segment((41,28)).segment((25,28)).segment((25,45)).segment((40,45)).arc((22,54),(6,43)).segment((6,96)).segment((-83,96)).close().assemble().finalize().extrude(-117).union(w1.sketch().segment((-96,-100),(-29,-100)).segment((-29,15)).segment((-69,15)).segment((-69,10)).segment((-96,10)).close().assemble().push([(-62,-42)]).circle(30,mode='s').finalize().extrude(-82))