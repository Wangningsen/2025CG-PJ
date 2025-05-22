import cadquery as cq
w0=cq.Workplane('YZ',origin=(-42,0,0))
w1=cq.Workplane('YZ',origin=(-75,0,0))
r=w0.sketch().segment((-41,-46),(44,-49)).segment((44,-10)).arc((54,-2),(60,9)).segment((60,27)).segment((44,27)).segment((44,39)).segment((31,38)).segment((32,27)).segment((-23,29)).arc((-90,70),(-39,11)).close().assemble().finalize().extrude(-33).union(w0.workplane(offset=117/2).moveTo(72,-56).cylinder(117,28)).union(w1.sketch().push([(51,-43)]).rect(12,10).push([(51.5,-43)]).rect(3,8,mode='s').finalize().extrude(18))