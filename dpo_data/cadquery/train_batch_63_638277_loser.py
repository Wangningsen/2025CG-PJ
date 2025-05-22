import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,46))
w1=cq.Workplane('XY',origin=(0,0,24))
r=w0.sketch().arc((-29,-21),(-100,-39),(-29,-50)).close().assemble().push([(-16,-8.5)]).rect(26,95).finalize().extrude(-93).union(w1.sketch().segment((56,-49),(100,-49)).segment((100,73)).segment((56,73)).segment((56,56)).arc((58,55),(56,54)).close().assemble().finalize().extrude(9))