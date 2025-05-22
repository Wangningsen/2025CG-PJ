import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,2,0))
w1=cq.Workplane('XY',origin=(0,0,45))
r=w0.sketch().segment((-30,-70),(-13,-46)).segment((-13,-47)).arc((24,-32),(64,-40)).arc((-22,73),(-30,-70)).assemble().finalize().extrude(57).union(w1.sketch().push([(0,-33)]).rect(200,52).rect(46,24,mode='s').finalize().extrude(-38))