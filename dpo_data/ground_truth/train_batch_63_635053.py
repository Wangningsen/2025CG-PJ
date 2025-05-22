import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,29,0))
r=w0.sketch().arc((1,-51),(-26,-81),(15,-80)).arc((96,-25),(1,-51)).assemble().push([(-6,-72)]).circle(3,mode='s').finalize().extrude(-58).union(w0.workplane(offset=-24/2).moveTo(-57,52).cylinder(24,43))