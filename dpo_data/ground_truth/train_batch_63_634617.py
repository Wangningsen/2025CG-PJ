import cadquery as cq
w0=cq.Workplane('YZ',origin=(-13,0,0))
w1=cq.Workplane('XY',origin=(0,0,-70))
r=w0.sketch().segment((-84,-50),(-81,-50)).arc((-20,-97),(41,-50)).segment((44,-50)).segment((44,-17)).segment((41,-17)).arc((-20,29),(-81,-17)).segment((-84,-17)).close().assemble().push([(8.5,87.5)]).rect(151,19).rect(11,17,mode='s').finalize().extrude(113).union(w1.sketch().segment((-81,-39),(22,-39)).segment((22,-34)).segment((60,-34)).segment((60,-6)).segment((22,-6)).segment((22,27)).segment((-2,27)).arc((-75,63),(-81,-18)).close().assemble().finalize().extrude(92))