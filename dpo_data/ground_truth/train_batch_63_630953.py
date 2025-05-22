import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
w1=cq.Workplane('YZ',origin=(-39,0,0))
r=w0.workplane(offset=-73/2).moveTo(-46,35.5).box(92,47,73).union(w0.sketch().segment((16,100),(50,66)).arc((41,91),(16,100)).assemble().finalize().extrude(-43)).union(w0.sketch().push([(-46,36)]).circle(8).push([(47.5,-57)]).rect(89,86).finalize().extrude(55)).union(w1.workplane(offset=-37/2).moveTo(-40,-41).cylinder(37,35))