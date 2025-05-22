import cadquery as cq
w0=cq.Workplane('YZ',origin=(-71,0,0))
r=w0.sketch().segment((-98,-20),(-40,-15)).segment((-38,-49)).segment((-85,-53)).arc((93,37),(-98,-20)).assemble().finalize().extrude(142)