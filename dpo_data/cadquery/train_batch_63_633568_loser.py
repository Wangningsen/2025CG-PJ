import cadquery as cq
w0=cq.Workplane('YZ',origin=(49,0,0))
r=w0.sketch().arc((-92,-8),(-93,-44),(-72,-73)).arc((90,35),(-92,-8)).assemble().finalize().extrude(-98)