import cadquery as cq
w0=cq.Workplane('YZ',origin=(-19,0,0))
r=w0.sketch().arc((-64,-46),(-96,-77),(-56,-57)).arc((83,52),(-64,-46)).assemble().finalize().extrude(38)