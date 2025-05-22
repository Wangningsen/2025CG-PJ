import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-10,0))
r=w0.sketch().arc((-96,-29),(87,49),(-71,-71)).arc((-54,-72),(-39,-78)).arc((61,65),(-88,-12)).arc((-93,-20),(-96,-29)).assemble().finalize().extrude(20)