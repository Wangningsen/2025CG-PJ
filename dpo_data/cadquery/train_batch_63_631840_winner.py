import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-45))
r=w0.sketch().segment((-44,-24),(-26,-25)).arc((-12,-100),(4,-26)).segment((47,-27)).segment((51,97)).segment((-40,100)).close().assemble().push([(-12,-61)]).rect(34,14,mode='s').finalize().extrude(89)