import cadquery as cq
w0=cq.Workplane('YZ',origin=(54,0,0))
r=w0.sketch().arc((18,-55),(16,-85),(44,-77)).arc((53,-41),(18,-55)).assemble().finalize().extrude(-108).union(w0.sketch().push([(-43.5,-44.5)]).rect(113,15).push([(39,31)]).circle(61).finalize().extrude(-50))