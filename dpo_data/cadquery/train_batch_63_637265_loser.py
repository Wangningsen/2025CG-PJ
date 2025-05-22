import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,27,0))
r=w0.workplane(offset=-54/2).moveTo(0,-22).cylinder(54,30).union(w0.sketch().push([(-97.5,-66.5)]).rect(5,19).push([(-97,-67)]).circle(2,mode='s').push([(-32.5,-66.5)]).rect(5,19).push([(66.5,47)]).rect(67,58).finalize().extrude(-48))