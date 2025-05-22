import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,18))
w1=cq.Workplane('ZX',origin=(0,-5,0))
r=w0.sketch().segment((70,66),(94,24)).arc((97,53),(70,66)).assemble().finalize().extrude(-106).union(w0.workplane(offset=69/2).moveTo(-43,-7.5).box(8,59,69)).union(w1.workplane(offset=-61/2).moveTo(36.5,-41).box(25,118,61))