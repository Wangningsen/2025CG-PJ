import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,42,0))
w1=cq.Workplane('ZX',origin=(0,47,0))
r=w0.sketch().push([(-80,37)]).circle(20).push([(-79.5,37.5)]).rect(13,31,mode='s').finalize().extrude(-93).union(w0.sketch().push([(21,-14)]).circle(50).push([(20.5,-13.5)]).rect(15,73,mode='s').finalize().extrude(-88)).union(w0.sketch().push([(26,20.5)]).rect(100,91).push([(89.5,80.5)]).rect(21,33).finalize().extrude(-79)).union(w1.workplane(offset=3/2).moveTo(4,-82).cylinder(3,15))