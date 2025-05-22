import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,67))
w1=cq.Workplane('ZX',origin=(0,1,0))
r=w0.sketch().segment((-59,-41),(2,-41)).segment((23,-41)).segment((59,-41)).segment((59,61)).segment((-59,61)).close().assemble().finalize().extrude(33).union(w1.sketch().segment((-100,-15),(-95,-15)).arc((-98,-5),(-100,5)).close().assemble().finalize().extrude(-62))