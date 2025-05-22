import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,3,0))
r=w0.sketch().push([(-82,11.5)]).rect(36,59).push([(-77,16)]).circle(8,mode='s').push([(-29,-53.5)]).rect(30,11).finalize().extrude(-39).union(w0.workplane(offset=25/2).moveTo(-1,-12).cylinder(25,12)).union(w0.sketch().push([(50.5,54.5)]).rect(99,9).rect(3,5,mode='s').finalize().extrude(33))