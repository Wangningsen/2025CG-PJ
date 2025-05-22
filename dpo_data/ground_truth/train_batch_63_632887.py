import cadquery as cq
w0=cq.Workplane('YZ',origin=(67,0,0))
r=w0.sketch().arc((-4,-75),(96,-36),(40,56)).arc((-96,29),(-4,-75)).assemble().finalize().extrude(-134)