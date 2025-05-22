import cadquery as cq
w0=cq.Workplane('YZ',origin=(-38,0,0))
w1=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().push([(6,-10)]).circle(34).push([(41,63)]).rect(50,74).finalize().extrude(58).union(w0.sketch().push([(-3,-75.5)]).rect(2,49).push([(-3,-75)]).rect(2,2,mode='s').finalize().extrude(76)).union(w1.workplane(offset=-77/2).moveTo(-10,-18).cylinder(77,1))