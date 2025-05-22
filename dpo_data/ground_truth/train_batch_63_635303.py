import cadquery as cq
w0=cq.Workplane('YZ',origin=(70,0,0))
r=w0.sketch().segment((-100,-20),(-94,-36)).segment((-1,1)).segment((-1,-48)).segment((-2,-48)).arc((25,-58),(54,-53)).segment((90,-57)).segment((100,44)).segment((64,47)).arc((36,58),(6,53)).segment((-29,57)).segment((-31,43)).segment((-1,43)).segment((-1,19)).close().assemble().finalize().extrude(-140)