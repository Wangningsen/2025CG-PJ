import cadquery as cq
w0=cq.Workplane('YZ',origin=(-56,0,0))
r=w0.sketch().segment((-13,35),(40,-6)).arc((25,31),(-13,35)).assemble().finalize().extrude(-44).union(w0.sketch().segment((40,-29),(48,-29)).arc((-52,4),(52,22)).segment((44,22)).arc((-45,4),(40,-29)).assemble().finalize().extrude(156))