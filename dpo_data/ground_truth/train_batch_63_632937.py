import cadquery as cq
w0=cq.Workplane('YZ',origin=(-14,0,0))
w1=cq.Workplane('ZX',origin=(0,17,0))
r=w0.sketch().push([(-82,-51)]).circle(18).reset().face(w0.sketch().segment((-1,-36),(5,-36)).segment((5,-29)).arc((16,-15),(5,-1)).segment((5,5)).segment((-1,5)).segment((-1,-1)).arc((-12,-15),(-1,-29)).close().assemble()).finalize().extrude(13).union(w1.workplane(offset=83/2).moveTo(28.5,12).box(81,4,83))