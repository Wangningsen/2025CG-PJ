import cadquery as cq
w0=cq.Workplane('YZ',origin=(-13,0,0))
w1=cq.Workplane('XY',origin=(0,0,22))
r=w0.sketch().segment((-84,-51),(-82,-51)).arc((-20,-97),(42,-51)).segment((44,-51)).segment((44,-20)).segment((42,-20)).arc((-20,29),(-82,-20)).segment((-84,-20)).close().assemble().push([(8.5,87.5)]).rect(151,19).rect(11,17,mode='s').finalize().extrude(113).union(w1.sketch().segment((-81,-39),(5,-39)).segment((5,44)).segment((-9,44)).arc((-83,58),(-81,-18)).close().assemble().finalize().extrude(-92))