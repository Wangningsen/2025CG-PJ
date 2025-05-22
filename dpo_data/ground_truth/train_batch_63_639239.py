import cadquery as cq
w0=cq.Workplane('YZ',origin=(-24,0,0))
w1=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.sketch().segment((-25,-39),(15,-61)).segment((19,-54)).arc((13,1),(62,26)).segment((69,39)).segment((29,61)).close().assemble().finalize().extrude(-76).union(w0.workplane(offset=-12/2).moveTo(-66,-53).cylinder(12,3)).union(w1.sketch().push([(22,0)]).rect(28,22).push([(34,-3)]).circle(3,mode='s').finalize().extrude(118))