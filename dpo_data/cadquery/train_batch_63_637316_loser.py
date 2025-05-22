import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
w1=cq.Workplane('YZ',origin=(-70,0,0))
r=w0.sketch().arc((-68,-66),(-34,-14),(-68,43)).segment((-68,25)).arc((-50,-14),(-68,-53)).close().assemble().finalize().extrude(-124).union(w0.workplane(offset=76/2).moveTo(35.5,66.5).box(69,17,76)).union(w1.workplane(offset=67/2).moveTo(-71.5,16).box(7,100,67))