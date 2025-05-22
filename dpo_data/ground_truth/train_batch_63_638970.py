import cadquery as cq
w0=cq.Workplane('YZ',origin=(-76,0,0))
w1=cq.Workplane('ZX',origin=(0,-85,0))
r=w0.sketch().segment((-25,2),(-6,-38)).segment((-15,-42)).segment((6,-100)).segment((73,-77)).segment((37,24)).close().assemble().finalize().extrude(75).union(w0.workplane(offset=171/2).moveTo(-56,32.5).box(64,43,171)).union(w1.sketch().arc((6,-87),(45,-93),(74,-67)).arc((4,66),(6,-84)).close().assemble().finalize().extrude(173))