import cadquery as cq
w0=cq.Workplane('YZ',origin=(-51,0,0))
w1=cq.Workplane('XY',origin=(0,0,20))
r=w0.workplane(offset=63/2).moveTo(65,-56).cylinder(63,35).union(w0.sketch().push([(12.5,37.5)]).rect(29,47).push([(-1.5,52.5)]).rect(1,1,mode='s').push([(1,35)]).circle(2,mode='s').finalize().extrude(64)).union(w1.sketch().segment((-25,-94),(1,-94)).arc((13,-100),(25,-94)).segment((51,-94)).segment((51,-77)).segment((25,-77)).arc((13,-70),(1,-77)).segment((-25,-77)).close().assemble().finalize().extrude(71))