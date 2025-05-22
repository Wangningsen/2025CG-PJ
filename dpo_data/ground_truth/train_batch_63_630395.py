import cadquery as cq
w0=cq.Workplane('YZ',origin=(54,0,0))
r=w0.sketch().arc((17,-66),(22,-90),(43,-78)).arc((46,-36),(17,-66)).assemble().finalize().extrude(-108).union(w0.sketch().push([(-43,-44.5)]).rect(114,15).reset().face(w0.sketch().arc((-11,-8),(-6,-13),(0,-15)).arc((80,76),(-6,-9)).close().assemble()).finalize().extrude(-50))