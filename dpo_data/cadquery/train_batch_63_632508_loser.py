import cadquery as cq
w0=cq.Workplane('YZ',origin=(-39,0,0))
r=w0.sketch().arc((-84,23),(-60,58),(-46,15)).arc((-45,98),(-84,23)).assemble().push([(40,-40)]).circle(60).finalize().extrude(78)