import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.workplane(offset=-200/2).cylinder(200,29).union(w0.sketch().rect(38,40).push([(5.5,6.5)]).rect(5,23,mode='s').push([(11.5,-17)]).rect(3,4,mode='s').push([(12.5,17.5)]).rect(3,5,mode='s').finalize().extrude(-195))