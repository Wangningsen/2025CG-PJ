import cadquery as cq
w0=cq.Workplane('YZ',origin=(-54,0,0))
r=w0.sketch().arc((70,-96),(69,-90),(74,-92)).arc((45,-64),(70,-96)).assemble().finalize().extrude(99).union(w0.workplane(offset=107/2).moveTo(-22.5,41).box(111,118,107))