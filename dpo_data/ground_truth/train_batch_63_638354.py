import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,47))
r=w0.sketch().arc((-63,-45),(-1,-99),(37,-25)).segment((74,-25)).segment((74,100)).segment((-58,100)).segment((-58,-25)).segment((1,-25)).arc((-27,-49),(-63,-45)).assemble().finalize().extrude(-94).union(w0.workplane(offset=-32/2).moveTo(-11,-47.5).box(126,99,32))