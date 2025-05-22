import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
r=w0.workplane(offset=18/2).moveTo(-95,-88).cylinder(18,5).union(w0.sketch().segment((43,85),(100,53)).arc((82,88),(43,85)).assemble().finalize().extrude(77))