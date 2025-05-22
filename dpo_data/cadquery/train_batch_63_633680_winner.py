import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
r=w0.sketch().arc((-26,-8),(50,-93),(17,17)).arc((-53,94),(-26,-8)).assemble().push([(-28,47)]).circle(15,mode='s').finalize().extrude(-15)