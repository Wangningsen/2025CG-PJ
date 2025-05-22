import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-30,0))
w1=cq.Workplane('YZ',origin=(-28,0,0))
r=w0.sketch().push([(-61,0)]).circle(39).reset().face(w0.sketch().segment((-90,27),(-85,1)).segment((-85,0)).segment((-84,0)).arc((-81,0),(-79,-2)).segment((-40,1)).segment((-40,2)).segment((-67,27)).close().assemble(),mode='s').push([(-54,-32)]).rect(12,4,mode='s').finalize().extrude(56).union(w1.sketch().segment((15,-65),(86,-65)).segment((86,58)).segment((36,58)).arc((-83,58),(15,-12)).close().assemble().push([(-23,38)]).circle(17,mode='s').finalize().extrude(58))