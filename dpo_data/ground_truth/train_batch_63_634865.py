import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('XY',origin=(0,0,-20))
r=w0.sketch().segment((-100,64),(-94,57)).arc((-91,41),(-76,36)).segment((-69,28)).segment((-58,38)).segment((-64,46)).arc((-67,62),(-82,67)).segment((-88,74)).close().assemble().finalize().extrude(48).union(w0.sketch().arc((24,-37),(13,-4),(38,19)).arc((-42,11),(24,-37)).assemble().finalize().extrude(60)).union(w1.workplane(offset=-54/2).moveTo(-44,75).cylinder(54,25))