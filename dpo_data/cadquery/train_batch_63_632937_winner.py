import cadquery as cq
w0=cq.Workplane('YZ',origin=(-1,0,0))
w1=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().push([(-82,-51)]).circle(18).reset().face(w0.sketch().segment((-1,-36),(5,-36)).segment((5,-29)).arc((16,-15),(5,-1)).segment((5,5)).segment((-1,5)).segment((-1,-1)).arc((-12,-15),(-1,-29)).close().assemble()).finalize().extrude(-13).union(w1.workplane(offset=81/2).moveTo(12,58.5).box(4,83,81))