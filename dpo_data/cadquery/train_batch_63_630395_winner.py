import cadquery as cq
w0=cq.Workplane('YZ',origin=(54,0,0))
r=w0.sketch().arc((17,-64),(22,-90),(43,-77)).arc((45,-36),(17,-64)).assemble().finalize().extrude(-108).union(w0.sketch().push([(-45.5,-44.5)]).rect(109,15).push([(39,31)]).circle(61).finalize().extrude(-50))