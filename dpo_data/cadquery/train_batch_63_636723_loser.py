import cadquery as cq
w0=cq.Workplane('YZ',origin=(2,0,0))
r=w0.sketch().push([(-21.5,-94.5)]).rect(13,11).push([(-10,91)]).circle(9).finalize().extrude(-41).union(w0.sketch().segment((-18,-5),(-4,-5)).arc((28,0),(-3,10)).segment((-3,58)).segment((-18,58)).close().assemble().finalize().extrude(37))