import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
r=w0.sketch().segment((-59,6),(7,-6)).segment((25,86)).segment((-41,100)).close().assemble().push([(29.5,-85.5)]).rect(59,29).push([(29.5,-85)]).rect(9,4,mode='s').finalize().extrude(3).union(w0.sketch().segment((-22,-28),(-12,-66)).segment((-3,-64)).segment((-12,-25)).close().assemble().finalize().extrude(34))