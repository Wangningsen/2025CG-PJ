import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
w1=cq.Workplane('XY',origin=(0,0,1))
r=w0.sketch().segment((-83,-19),(6,-19)).segment((6,26)).arc((27,15),(43,33)).segment((25,33)).segment((25,46)).segment((39,46)).arc((22,54),(6,43)).segment((6,96)).segment((-83,96)).close().assemble().finalize().extrude(117).union(w1.sketch().segment((-96,-100),(-29,-100)).segment((-29,15)).segment((-70,15)).segment((-70,10)).segment((-96,10)).close().assemble().push([(-62,-42)]).circle(30,mode='s').finalize().extrude(82))