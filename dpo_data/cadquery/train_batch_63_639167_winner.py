import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
w1=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().arc((55,36),(53,38),(56,38)).arc((46,39),(55,36)).assemble().finalize().extrude(-31).union(w1.sketch().push([(-49,-77)]).rect(102,12).push([(45.5,26.5)]).rect(109,113).finalize().extrude(-31))