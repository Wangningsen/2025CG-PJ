import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,66))
w1=cq.Workplane('XY',origin=(0,0,24))
r=w0.workplane(offset=-100/2).moveTo(-36.5,-71.5).box(67,7,100).union(w0.workplane(offset=34/2).moveTo(35.5,66.5).box(69,17,34)).union(w1.sketch().arc((-68,25),(-50,-13),(-68,-48)).segment((-68,-66)).arc((-34,-13),(-68,43)).segment((-68,25)).assemble().finalize().extrude(-124))