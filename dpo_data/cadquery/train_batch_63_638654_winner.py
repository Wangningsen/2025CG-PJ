import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('YZ',origin=(22,0,0))
r=w0.sketch().arc((-46,1),(-61,-82),(23,-77)).arc((74,-30),(51,35)).segment((51,54)).segment((31,54)).arc((6,59),(-18,54)).segment((-30,54)).segment((-30,44)).arc((-42,27),(-46,10)).close().assemble().finalize().extrude(94).union(w1.sketch().segment((-8,42),(67,42)).segment((67,46)).segment((69,46)).segment((69,64)).segment((67,64)).segment((67,100)).segment((-8,100)).close().assemble().finalize().extrude(-95))