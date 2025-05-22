import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('ZX',origin=(0,-8,0))
r=w0.sketch().arc((-46,-1),(-59,-84),(24,-77)).arc((74,-12),(19,51)).segment((19,54)).segment((13,54)).arc((4,59),(-5,54)).segment((-31,54)).segment((-31,43)).arc((-42,26),(-46,6)).close().assemble().finalize().extrude(94).union(w1.sketch().segment((42,-73),(100,-73)).segment((100,22)).segment((64,22)).arc((59,23),(54,22)).segment((42,22)).close().assemble().finalize().extrude(75))