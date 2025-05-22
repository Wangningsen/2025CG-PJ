import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,22))
w1=cq.Workplane('ZX',origin=(0,75,0))
r=w0.sketch().arc((-100,-35),(-6,-50),(-63,26)).arc((-47,-25),(-100,-35)).assemble().finalize().extrude(-113).union(w0.workplane(offset=-90/2).moveTo(46,48).cylinder(90,15)).union(w1.sketch().arc((-18,36),(-62,20),(-16,28)).arc((89,59),(-18,36)).assemble().finalize().extrude(-96))