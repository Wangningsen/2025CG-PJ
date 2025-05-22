import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
r=w0.sketch().arc((-92,-39),(-60,-59),(-46,-90)).arc((75,67),(-92,-39)).assemble().finalize().extrude(68)