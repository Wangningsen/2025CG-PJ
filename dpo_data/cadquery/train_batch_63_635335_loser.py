import cadquery as cq
w0=cq.Workplane('YZ',origin=(82,0,0))
w1=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().segment((-87,-58),(-72,-58)).arc((-26,-74),(20,-58)).segment((36,-58)).segment((36,-41)).arc((48,0),(36,41)).segment((36,58)).segment((20,58)).arc((-26,74),(-72,58)).segment((-87,58)).segment((-87,41)).arc((-100,0),(-87,-41)).close().assemble().push([(-43,37)]).circle(16,mode='s').finalize().extrude(-164).union(w1.workplane(offset=67/2).moveTo(59,11).cylinder(67,4))