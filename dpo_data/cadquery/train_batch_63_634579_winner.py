import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().push([(-89.5,-54)]).rect(21,72).push([(-93,-28)]).circle(6,mode='s').finalize().extrude(-32).union(w0.sketch().arc((49,78),(-16,30),(64,28)).arc((99,66),(49,83)).close().assemble().finalize().extrude(-4))