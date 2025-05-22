import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-84,-8),(-16,-8)).segment((-16,-6)).segment((-8,-6)).segment((-8,-8)).segment((84,-8)).segment((84,8)).segment((-84,8)).close().assemble().finalize().extrude(-200)