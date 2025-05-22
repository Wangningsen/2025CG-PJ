import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,15,0))
r=w0.sketch().arc((-39,25),(6,12),(8,57)).arc((-52,93),(-39,25)).assemble().push([(63,-95)]).circle(5).finalize().extrude(-30)