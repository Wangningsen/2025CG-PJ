import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.sketch().arc((-40,25),(4,11),(8,57)).arc((-51,94),(-40,25)).assemble().push([(63,-95)]).circle(5).finalize().extrude(30)