import cadquery as cq
w0=cq.Workplane('YZ',origin=(-19,0,0))
r=w0.sketch().arc((-66,-43),(-97,-76),(-54,-57)).arc((85,50),(-66,-43)).assemble().finalize().extrude(38)