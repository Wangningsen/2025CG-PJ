import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,40,0))
r=w0.sketch().push([(20,51)]).circle(49).push([(20.5,51)]).rect(9,64,mode='s').finalize().extrude(-105).union(w0.workplane(offset=-8/2).moveTo(-24,-55.5).box(44,55,8)).union(w0.workplane(offset=25/2).moveTo(-24,-56).cylinder(25,44))