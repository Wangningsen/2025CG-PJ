import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
w1=cq.Workplane('XY',origin=(0,0,-40))
r=w0.sketch().arc((-4,-14),(-11,-31),(7,-36)).arc((95,21),(-4,-14)).assemble().finalize().extrude(-79).union(w1.sketch().segment((-100,-4),(-47,-4)).segment((-47,7)).segment((-35,7)).segment((-35,44)).segment((-47,44)).segment((-47,54)).segment((-100,54)).close().assemble().push([(-66,39.5)]).rect(6,23,mode='s').finalize().extrude(122))