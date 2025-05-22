import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,61))
r=w0.sketch().arc((-62,7),(-65,-46),(-12,-35)).segment((38,-35)).segment((38,100)).segment((-62,100)).close().assemble().finalize().extrude(-144).union(w0.sketch().push([(1.5,-75)]).rect(149,50).push([(2,-75)]).circle(6,mode='s').finalize().extrude(22))