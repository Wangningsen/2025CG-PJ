import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,60))
r=w0.workplane(offset=-120/2).moveTo(-44.5,-7.5).box(111,37,120).union(w0.sketch().segment((-73,-36),(-58,-46)).segment((-16,21)).segment((-32,31)).close().assemble().finalize().extrude(-88)).union(w0.workplane(offset=-62/2).moveTo(85,31).cylinder(62,15))