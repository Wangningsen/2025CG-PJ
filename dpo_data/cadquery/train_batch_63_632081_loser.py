import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
w1=cq.Workplane('YZ',origin=(85,0,0))
r=w0.sketch().push([(4,53)]).circle(47).push([(2,46.5)]).rect(42,29,mode='s').finalize().extrude(12).union(w0.sketch().push([(-38,-87)]).circle(13).push([(-34,-93)]).circle(3,mode='s').finalize().extrude(84)).union(w1.sketch().push([(-69,-1.5)]).rect(52,53).push([(-54,5)]).circle(2,mode='s').finalize().extrude(-170))