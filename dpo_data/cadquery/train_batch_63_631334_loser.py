import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.sketch().arc((-73,-81),(-57,-94),(-37,-99)).arc((-21,-99),(-6,-96)).arc((61,80),(-73,-64)).arc((-60,-73),(-73,-81)).assemble().finalize().extrude(6)