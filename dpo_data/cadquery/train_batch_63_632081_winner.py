import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
w1=cq.Workplane('YZ',origin=(-85,0,0))
r=w0.sketch().push([(4,53)]).circle(47).push([(-4.5,44)]).rect(37,58,mode='s').finalize().extrude(12).union(w0.workplane(offset=84/2).moveTo(-38,-87).cylinder(84,13)).union(w1.sketch().push([(-69,-1.5)]).rect(52,53).push([(-54,4)]).circle(2,mode='s').finalize().extrude(170))