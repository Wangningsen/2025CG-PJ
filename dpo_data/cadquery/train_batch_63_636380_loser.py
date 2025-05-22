import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,3,0))
r=w0.sketch().push([(-82,11.5)]).rect(36,59).push([(-77,16)]).circle(8,mode='s').push([(-29,-53.5)]).rect(30,11).finalize().extrude(-39).union(w0.sketch().push([(-1,-12)]).circle(13).push([(6,-5)]).circle(2,mode='s').finalize().extrude(25)).union(w0.workplane(offset=33/2).moveTo(50.5,54.5).box(99,9,33))