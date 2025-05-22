import cadquery as cq
w0=cq.Workplane('YZ',origin=(18,0,0))
r=w0.sketch().push([(-11,93.5)]).rect(64,13).push([(-14,83)]).rect(22,2).finalize().extrude(-36).union(w0.sketch().segment((-14,-96),(-5,-100)).segment((43,7)).segment((34,11)).close().assemble().finalize().extrude(-27))