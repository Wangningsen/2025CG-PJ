import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
w1=cq.Workplane('YZ',origin=(-41,0,0))
r=w0.workplane(offset=9/2).moveTo(10.5,82.5).box(61,35,9).union(w0.sketch().push([(2,-72)]).rect(40,56).push([(0,-67)]).circle(9,mode='s').finalize().extrude(63)).union(w1.sketch().arc((-37,-12),(-36,-15),(-34,-19)).arc((-35,-15),(-37,-12)).assemble().finalize().extrude(36))