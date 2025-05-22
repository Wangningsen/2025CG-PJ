import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-41,0))
w1=cq.Workplane('XY',origin=(0,0,-50))
r=w0.sketch().segment((-54,-44),(-28,-44)).segment((-28,-43)).segment((13,-60)).segment((13,-61)).segment((15,-61)).segment((16,-62)).segment((17,-61)).segment((74,-61)).arc((62,-18),(26,7)).arc((-31,98),(-39,-12)).arc((-46,-24),(-50,-37)).segment((-54,-37)).close().assemble().finalize().extrude(103).union(w1.sketch().push([(-96,-59)]).circle(4).circle(3,mode='s').finalize().extrude(64))